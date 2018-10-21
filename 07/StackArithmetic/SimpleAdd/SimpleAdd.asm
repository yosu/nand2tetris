// constant to D
@7
D=A
// push D to stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// constant to D
@8
D=A
// push D to stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// decrement stack pointer
@SP
M=M-1
// pop stack to D
A=M
D=M
// decrement stack pointer
@SP
M=M-1
A=M
// add D on the stack
M=D+M
// increment stack pointer
@SP
M=M+1
