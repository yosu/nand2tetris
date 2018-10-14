#!/usr/bin/env python
import sys
from typing import *
from enum import Enum, auto


VAR_START = 16


class CommandType(Enum):
    A_COMMAND = auto()
    C_COMMAND = auto()
    L_COMMAND = auto()


class ReservedAddress(Enum):
    SP = 0
    LCL = 1
    ARG = 2
    THIS = 3
    THAT = 4
    SCREEN = 0x4000
    KBD = 0x6000


class ReservedRegister(Enum):
    R0 = 0
    R1 = 1
    R2 = 2
    R3 = 3
    R4 = 4
    R5 = 5
    R6 = 6
    R7 = 7
    R8 = 8
    R9 = 9
    R10 = 10
    R11 = 11
    R12 = 12
    R13 = 13
    R14 = 14
    R15 = 15


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


class SymbolTable:
    def __init__(self):
        self.table = {}

    def add_entry(self, symbol: str, address: int):
        self.table[symbol] = address

    def contains(self, symbol: str) -> bool:
        return symbol in self.table

    def get_address(self, symbol: str) -> int:
        return self.table[symbol]


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

    def parse(self, line: str) -> bool:
        cmd = self._extract_command(line)

        if not cmd:
            return False

        if cmd[0] == '@':
            self.next_command_type = CommandType.A_COMMAND
            self.next_symbol = self.parse_a_command(cmd)
        elif cmd[0] == '(':
            self.next_command_type = CommandType.L_COMMAND
            self.next_symbol = self.parse_l_command(cmd)
        else:
            self.next_command_type = CommandType.C_COMMAND
            self.next_dest, self.next_comp, self.next_jump = self.parse_c_command(cmd)

        return True

    # A instruction
    # @value
    def parse_a_command(self, cmd: str) -> str:
        # @Xxx -> Xxx
        return cmd[1:]

    # psuedo command
    # (Xxx)
    def parse_l_command(self, cmd: str) -> str:
        # (Xxx) -> Xxx
        return cmd[1:-1]

    # C instruction
    # dest=comp;jump
    def parse_c_command(self, cmd: str) -> Tuple[Optional[str], str, Optional[str]]:
        word = ''
        for i, c in enumerate(cmd):
            # omit `=' if dest is empty
            if c == ';':
                return None, word, cmd[i+1:]

            # omit `;' if jump is empty
            if c == '=':
                return word, cmd[i+1:], None

            word += c

        raise ValueError(f'Error: can not parse {cmd}')

    def _extract_command(self, line: str) -> str:
        s = self._remove_white_space(line)
        return self._remove_comment(s)

    def _remove_white_space(self, line: str) -> str:
        acc = ''
        for c in line:
            if not c.isspace():
                acc += c

        return acc

    def _remove_comment(self, line: str) -> str:
        for i, c in enumerate(line):
            if c == '/' and i < len(line) and line[i+1] == '/':
                return line[0:i]

        return line


def load_symbol(_in) -> SymbolTable:
    table = SymbolTable()

    for reserved in ReservedAddress:
        table.add_entry(reserved.name, reserved.value)

    for reserved in ReservedRegister:
        table.add_entry(reserved.name, reserved.value)

    address = 0

    parser = Parser(_in)
    parser.advance()
    while parser.has_more_commands:
        parser.advance()
        if parser.command_type == CommandType.L_COMMAND:
            if not table.contains(parser.symbol):
                table.add_entry(parser.symbol, address)
                continue

        address += 1

    return table


def parse(_in, table: SymbolTable):
    variable_address = VAR_START
    parser = Parser(_in)
    parser.advance()
    while parser.has_more_commands:
        parser.advance()
        if parser.command_type == CommandType.A_COMMAND:
            address = None
            symbol = parser.symbol
            if symbol[0].isdigit():
                address = int(symbol)
            else:
                if table.contains(symbol):
                    address = table.get_address(symbol)
                else:
                    # variable definition
                    address = variable_address
                    variable_address += 1

                    table.add_entry(symbol, address)

            if address is not None:
                print(f'{address:016b}')

        elif parser.command_type == CommandType.C_COMMAND:
            hack = ['111',
                    Code.comp(parser.comp),
                    Code.dest(parser.dest),
                    Code.jump(parser.jump)]
            print(''.join(hack))
        elif parser.command_type == CommandType.L_COMMAND:
            continue
        else:
            print('the command id not supported: {}'.format(parser.command_type))
            sys.exit(1)


def main():
    table = load_symbol(sys.stdin)
    sys.stdin.seek(0)
    parse(sys.stdin, table)


if __name__ == '__main__':
    main()
