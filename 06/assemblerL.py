#!/usr/bin/env python
import sys
from typing import *
from enum import Enum, auto


class CommandType(Enum):
    A_COMMAND = auto()
    C_COMMAND = auto()
    L_COMMAND = auto()


class Code:
    jumps = {
        'null': '000',
        'JGT': '001',
        'JEQ': '010',
        'JGE': '011',
        'JLT': '100',
        'JNE': '101',
        'JLE': '110',
        'JMP': '111',
    }

    comps = {
        '0':    '0101010',
        '1':    '0111111',
        '-1':   '0111010',
        'D':    '0001100',
        'A':    '0110000',
        '!D':   '0001101',
        '!A':   '0110001',
        '-D':   '0001111',
        '-A':   '0110011',
        'D+1':  '0011111',
        'A+1':  '0110111',
        'D-1':  '0001110',
        'A-1':  '0110010',
        'D+A':  '0000010',
        'D-A':  '0010011',
        'A-D':  '0000111',
        'D&A':  '0000000',
        'D|A':  '0010101',
        'M':    '1110000',
        '!M':   '1110001',
        '-M':   '1110011',
        'M+1':  '1110111',
        'M-1':  '1110010',
        'D+M':  '1000010',
        'D-M':  '1010011',
        'M-D':  '1000111',
        'D&M':  '1000000',
        'D|M':  '1010101',
    }

    dests = {
        'null': '000',
        'M':    '001',
        'D':    '010',
        'MD':   '011',
        'A':    '100',
        'AM':   '101',
        'AD':   '110',
        'AMD':  '111',
    }

    @classmethod
    def jump(cls, mnemonic):
        if not mnemonic:
            mnemonic = 'null'

        return cls.jumps[mnemonic]

    @classmethod
    def dest(cls, mnemonic):
        if not mnemonic:
            mnemonic = 'null'

        hack = cls.dests.get(mnemonic)

        if hack:
            return hack

        num = int(mnemonic)
        return f'{num:03b}'

    @classmethod
    def comp(cls, mnemonic):
        return cls.comps[mnemonic]


class Parser:
    def __init__(self, _in):
        self._in = _in
        self.has_more_commands = False
        self.command_type = None
        self.symbol = None
        self.dest = None
        self.comp = None
        self.jump = None

        self.next_command_type = None
        self.next_symbol = None
        self.next_dest = None
        self.next_comp = None
        self.next_jump = None

    def advance(self):
        if self.has_more_commands:
            self.command_type = self.next_command_type
            self.symbol = self.next_symbol
            self.dest = self.next_dest
            self.comp = self.next_comp
            self.jump = self.next_jump

        for line in self._in:
            if self.parse(line):
                self.has_more_commands = True
                return

        self.has_more_commands = False

    def parse(self, line: str):
        s = self._extract_command(line)

        if not s:
            return False

        if s[0] == '@':
            self.next_command_type = CommandType.A_COMMAND
            self.next_symbol = self.parse_a_command(s[1:])
        else:
            self.next_command_type = CommandType.C_COMMAND
            self.next_dest, self.next_comp, self.next_jump = self.parse_c_command(s)

        return True

    def parse_a_command(self, s: str):
        return  int(s)

    # C命令
    # dest=comp;jump
    def parse_c_command(self, s: str):
        word = ''
        for i, c in enumerate(s):
            # destが空であれば「=」は省略される
            if c == ';':
                return None, word, s[i+1:]

            # jumpが空であれば「;」は省略される
            if c == '=':
                return word, s[i+1:], None

            word += c

        raise ValueError(f'Error: can not parse {s}')

    def _extract_command(self, line):
        s = self._remove_white_space(line)
        return self._remove_comment(s)

    def _remove_white_space(self, line):
        acc = ''
        for c in line:
            if not c.isspace():
                acc += c

        return acc

    def _remove_comment(self, line):
        for i, c in enumerate(line):
            if c == '/' and i < len(line) and line[i+1] == '/':
                return line[0:i]

        return line


def main():
    parser = Parser(sys.stdin)
    parser.advance()
    while parser.has_more_commands:
        parser.advance()
        if parser.command_type == CommandType.A_COMMAND:
            print(f'{parser.symbol:016b}')
        elif parser.command_type == CommandType.C_COMMAND:
            hack = ['111',
                    Code.comp(parser.comp),
                    Code.dest(parser.dest),
                    Code.jump(parser.jump)]
            print(''.join(hack))
        else:
            print('the command id not supported: {}'.format(parser.command_type))
            sys.exit(1)

if __name__ == '__main__':
    main()
