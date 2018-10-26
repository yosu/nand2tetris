#!/usr/bin/env python
import re
import sys
import textwrap
from enum import Enum, auto
from io import StringIO
from pathlib import PurePath


class Command(Enum):
    # Arithmetic Command
    ADD = 'add'
    SUB = 'sub'
    NEG = 'neg'
    EQ  = 'eq'
    GT  = 'gt'
    LT  = 'lt'
    AND = 'and'
    OR  = 'or'
    NOT = 'not'
    # Memory access command
    PUSH = 'push'
    POP  = 'pop'
    # Program flow command
    LABEL = 'label'
    GOTO  = 'goto'
    IF    = 'if-goto'
    # Function call command
    FUNCTION = 'function'
    CALL     = 'call'
    RETURN   = 'return'


class CommandType(Enum):
    C_ARITHMETIC = auto()
    C_PUSH = auto()
    C_POP = auto()
    C_LABEL = auto()
    C_GOTO = auto()
    C_IF = auto()
    C_FUNCTION = auto()
    C_RETURN = auto()
    C_CALL = auto()

    @classmethod
    def from_command(cls, cmd):
        return cls._command_type_map[cmd]


CommandType._command_type_map = {
    # Arithmetic Command
    Command.ADD: CommandType.C_ARITHMETIC,
    Command.SUB: CommandType.C_ARITHMETIC,
    Command.NEG: CommandType.C_ARITHMETIC,
    Command.EQ:  CommandType.C_ARITHMETIC,
    Command.GT:  CommandType.C_ARITHMETIC,
    Command.LT:  CommandType.C_ARITHMETIC,
    Command.AND: CommandType.C_ARITHMETIC,
    Command.OR:  CommandType.C_ARITHMETIC,
    Command.NOT: CommandType.C_ARITHMETIC,
    # Memory access command
    Command.PUSH: CommandType.C_PUSH,
    Command.POP:  CommandType.C_POP,
    # Program flow command
    Command.LABEL: CommandType.C_LABEL,
    Command.GOTO:  CommandType.C_GOTO,
    Command.IF:    CommandType.C_IF,
    # Function call command
    Command.FUNCTION: CommandType.C_FUNCTION,
    Command.CALL:     CommandType.C_CALL,
    Command.RETURN:   CommandType.C_RETURN
}


SEGMENTS = {
    'constant': None,
    'local': {
        'label': 'LCL',
        'register': 'M',
    },
    'argument': {
        'label': 'ARG',
        'register': 'M',
    },
    'this': {
        'label': 'THIS',
        'register': 'M',
    },
    'that': {
        'label': 'THAT',
        'register': 'M',
    },
    'pointer': {
        'label': 'THIS',
        'register': 'A',
    },
    'temp': {
        'label': 'R5',
        'register': 'A',
    },
}


class Text:
    def __init__(self, initial_text):
        self.text = initial_text
        self.cursor = 0

    def forward(self):
        if self.cursor >= len(self.text):
            return

        self.cursor += 1

    def backward(self):
        if self.cursor <= 0:
            return

        self.cursor -= 1

    def skip_space(self):
        while not self.end():
            if not self.current.isspace():
                return

            self.forward()

    @property
    def current(self):
        if self.end():
            raise ValueError("Current cursor is end")

        return self.text[self.cursor]

    def end(self):
        return len(self.text) <= self.cursor


class Parser:
    def __init__(self, _in):
        self._in = _in
        self.has_more_command = False

        self.command_type = None
        self.arg1 = None
        self.arg2 = None

        self.next_command_type = None
        self.next_arg1 = None
        self.next_arg2 = None

        self.advance()

    def advance(self):
        self.command_type = self.next_command_type
        self.arg1 = self.next_arg1
        self.arg2 = self.next_arg2

        for line in self._in:
            text = Text(line.rstrip())
            cmd = self._extract_command(text)

            if not cmd:
                continue

            self.has_more_command = True
            cmd_type, arg1, arg2 = self._extract_instruction(cmd, text)

            self.next_command_type = cmd_type
            self.next_arg1 = arg1
            self.next_arg2 = arg2
            return

        self.has_more_command = False

    def _extract_instruction(self, cmd, text):
        arg1, arg2 = None, None
        cmd_type = CommandType.from_command(cmd)

        if cmd_type == CommandType.C_ARITHMETIC:
            return cmd_type, cmd.value, None

        # binary args
        # TODO: Refactor
        if cmd_type == CommandType.C_PUSH or cmd_type == CommandType.C_POP:
            arg1 = self._extract_arg(text)
            arg2 = self._extract_arg(text)

            return cmd_type, arg1, arg2

        # program flow
        if cmd_type in [CommandType.C_LABEL, CommandType.C_GOTO, CommandType.C_IF] :
            arg1 = self._extract_arg(text)

            return cmd_type, arg1, None

        raise ValueError(f'Cannot extract args')

    def _extract_arg(self, text):
        text.skip_space()

        if text.end():
            raise ValueError('Cannot extract arg')

        arg = ''
        while not text.end() and not text.current.isspace():
            arg += text.current
            text.forward()

        return arg

    def _extract_command(self, text):
        text.skip_space()

        if text.end():
            return None

        # Comment line
        if text.current == '/':
            text.forward()
            if text.end() or text.current != '/':
                raise ValueError(f'Invalid command {line}')

            # Comment
            return None

        if not text.current.isalpha():
            raise ValueError(f'Command must be started at alphabet')

        cmd = ''
        while not text.end() and not text.current.isspace():
            cmd += text.current
            text.forward()

        return Command(cmd)


class CodeWriter:
    # Stack operation
    #
    # M: op1
    # D: op2
    bin_ops = {
        'add': 'D+M',
        'sub': 'M-D',
        'or': 'D|M',
        'and': 'D&M'
    }

    unu_ops = {
        'neg': '-M',
        'not': '!M'
    }

    cmp_ops = {
        'eq': 'JEQ',
        'lt': 'JLT',
        'gt': 'JGT'
    }

    def __init__(self, vm_file):
        self._out = None
        self.set_file_name(vm_file)
        self.label_counter = {}

    def set_file_name(self, vm_file):
        if self._out:
            self.close()

        asm_file = PurePath(vm_file).with_suffix('.asm')
        self._out = open(asm_file, 'w')

    def close(self):
        if self._out:
            close(self._out)
            self._out = None

    def write_label(self, label):
        self._validate_label(label)

        hack = f'''
        // ------------------------------------------------------------------------------
        // label {label}
        // ------------------------------------------------------------------------------
        (Label{label})
        '''

        self._write_text(hack)

    def write_goto(self, label):
        self._validate_label(label)

        hack = f'''
        // ------------------------------------------------------------------------------
        // goto {label}
        // ------------------------------------------------------------------------------
        @Label{label}
        0;JMP
        '''

        self._write_text(hack)

    def write_if(self, label):
        self._validate_label(label)

        hack = f'''
        // ------------------------------------------------------------------------------
        // if-goto {label}
        // ------------------------------------------------------------------------------
        # decrement stack pointer
        @SP
        M=M-1
        # pop stack to D
        A=M
        D=M
        @Label{label}
        D;JNE
        '''

        self._write_text(hack)

    def _validate_label(self, label):
        if re.search(r'[^A-Za-z0-9:._]', label):
            raise ValueError(f'Invalid label: {label}')

    def write_arithmetic(self, command):
        self._write_text(f'''
            // ------------------------------------------------------------------------------
            // {command}
            // ------------------------------------------------------------------------------
        ''')
        if command in self.bin_ops:
            op = self.bin_ops[command]

            hack = f'''
            # decrement stack pointer
            @SP
            M=M-1
            # pop stack to D
            A=M
            D=M
            # decrement stack pointer
            @SP
            M=M-1
            A=M
            # calculate on the stack
            M={op}
            # increment stack pointer
            @SP
            M=M+1
            '''
            self._write_text(hack)

        if command in self.unu_ops:
            op = self.unu_ops[command]

            hack = f'''
            # decrement stack pointer
            @SP
            M=M-1
            A=M
            # calculate on the stack
            M={op}
            # increment stack pointer
            @SP
            M=M+1
            '''
            self._write_text(hack)

        if command in self.cmp_ops:
            label = self._get_cmp_label(command)
            op = self.cmp_ops[command]

            hack = f'''
            # decrement stack pointer
            @SP
            M=M-1
            # pop stack to D
            A=M
            D=M
            # decrement stack pointer
            @SP
            M=M-1
            A=M
            # calculate on the stack
            D=M-D
            @{label}True
            D;{op}
            # set false to D
            D=0
            @{label}End
            0;JMP
            ({label}True)
            # set true to D
            D=-1
            ({label}End)
            # set result to the stack
            @SP
            A=M
            M=D
            # increment stack pointer
            @SP
            M=M+1
            '''
            self._write_text(hack)


    def _write_text(self, text):
        s = textwrap.dedent(text).lstrip()
        sio = StringIO(s)
        for line in sio:
            if line.startswith('#'):
                continue
            self._out.write(line)

    def write_push_pop(self, command_type, segment, index):
        if segment not in SEGMENTS:
            raise ValueError(f'Invalid segment specified: {segment}')

        if command_type == CommandType.C_PUSH:
            self._write_push(segment, index)
        if command_type == CommandType.C_POP:
            self._write_pop(segment, index)

    def _write_push(self, segment, index):
        self._write_text(f'''
            // ------------------------------------------------------------------------------
            // push {segment} {index}
            // ------------------------------------------------------------------------------
        ''')
        if segment == 'constant':
            hack = f'''
            # constant to D
            @{index}
            D=A
            # push D to stack
            @SP
            A=M
            M=D
            # increment stack pointer
            @SP
            M=M+1
            '''
            self._write_text(hack)
            return

        if segment in SEGMENTS:
            seg = SEGMENTS[segment]
            label = seg['label']
            register = seg['register']

            hack = f'''
            # get local address
            @{label}
            D={register}
            # move to local[index] address
            @{index}
            A=D+A
            # local[index] to D
            D=M
            # push D to stack
            @SP
            A=M
            M=D
            # increment stack pointer
            @SP
            M=M+1
            '''
            self._write_text(hack)

    def _write_pop(self, segment, index):
        self._write_text(f'''
            // ------------------------------------------------------------------------------
            // pop {segment} {index}
            // ------------------------------------------------------------------------------
        ''')
        if segment == 'constant':
            raise ValueError('`pop constant` is not supported')

        if segment in SEGMENTS:
            seg = SEGMENTS[segment]
            label = seg['label']
            register = seg['register']

            hack = f'''
            # get local address
            @{label}
            D={register}
            # move to local[index] address
            @{index}
            D=D+A
            # store to R13
            @R13
            M=D
            # decrement stack pointer
            @SP
            M=M-1
            # pop stack to D
            A=M
            D=M
            # get local[index] address
            @R13
            # D to local[index]
            A=M
            M=D
            '''
            self._write_text(hack)

    def _get_count(self, command: str):
        count = self.label_counter.get(command, 0)
        self.label_counter[command] = count + 1
        return self.label_counter[command]

    def _get_cmp_label(self, cmp_command: str) -> str:
        count = self._get_count(cmp_command)
        return cmp_command.capitalize() + str(count)


def process(vm_file):
    with open(vm_file, "r") as inh:
        parser = Parser(inh)

        writer = CodeWriter(vm_file)
        convert(parser, writer)


def convert(parser, writer):
    while parser.has_more_command:
        parser.advance()

        if parser.command_type == CommandType.C_ARITHMETIC:
            writer.write_arithmetic(parser.arg1)

        # TODO: Refactor
        if parser.command_type == CommandType.C_PUSH or parser.command_type == CommandType.C_POP:
            writer.write_push_pop(parser.command_type, parser.arg1, int(parser.arg2))

        if parser.command_type == CommandType.C_LABEL:
            writer.write_label(parser.arg1)

        if parser.command_type == CommandType.C_GOTO:
            writer.write_goto(parser.arg1)

        if parser.command_type == CommandType.C_IF:
            writer.write_if(parser.arg1)



def main():
    if len(sys.argv) < 2:
        print("Usage: vm_translator.py source")
        sys.exit(1)

    # TODO: ディレクトリのときはファイルを列挙して処理する
    vm_file = sys.argv[1]
    process(vm_file)


if __name__ == '__main__':
    main()
