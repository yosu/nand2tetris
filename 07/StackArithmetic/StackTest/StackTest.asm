// constant to D
@17
D=A
// push D to stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// constant to D
@17
D=A
// push D to stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// eq
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
// calculate on the stack
D=M-D
@Eq1True
D;JEQ
// set false to D
D=0
@Eq1End
0;JMP
(Eq1True)
// set true to D
D=-1
(Eq1End)
// set result to the stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// -----------------------
// constant to D
@17
D=A
// push D to stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// constant to D
@16
D=A
// push D to stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// eq
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
// calculate on the stack
D=M-D
@Eq2True
D;JEQ
// set false to D
D=0
@Eq2End
0;JMP
(Eq2True)
// set true to D
D=-1
(Eq2End)
// set result to the stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// -----------------------
// constant to D
@16
D=A
// push D to stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// constant to D
@17
D=A
// push D to stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// eq
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
// calculate on the stack
D=M-D
@Eq3True
D;JEQ
// set false to D
D=0
@Eq3End
0;JMP
(Eq3True)
// set true to D
D=-1
(Eq3End)
// set result to the stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// -----------------------
// constant to D
@892
D=A
// push D to stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// constant to D
@891
D=A
// push D to stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// lt
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
// calculate on the stack
D=M-D
@Lt1True
D;JLT
// set false to D
D=0
@Lt1End
0;JMP
(Lt1True)
// set true to D
D=-1
(Lt1End)
// set result to the stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// -----------------------
// constant to D
@891
D=A
// push D to stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// constant to D
@892
D=A
// push D to stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// lt
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
// calculate on the stack
D=M-D
@Lt2True
D;JLT
// set false to D
D=0
@Lt2End
0;JMP
(Lt2True)
// set true to D
D=-1
(Lt2End)
// set result to the stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// -----------------------
// constant to D
@891
D=A
// push D to stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// constant to D
@891
D=A
// push D to stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// lt
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
// calculate on the stack
D=M-D
@Lt3True
D;JLT
// set false to D
D=0
@Lt3End
0;JMP
(Lt3True)
// set true to D
D=-1
(Lt3End)
// set result to the stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// -----------------------
// constant to D
@32767
D=A
// push D to stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// constant to D
@32766
D=A
// push D to stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// gt
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
// calculate on the stack
D=M-D
@Gt1True
D;JGT
// set false to D
D=0
@Gt1End
0;JMP
(Gt1True)
// set true to D
D=-1
(Gt1End)
// set result to the stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// -----------------------
// constant to D
@32766
D=A
// push D to stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// constant to D
@32767
D=A
// push D to stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// gt
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
// calculate on the stack
D=M-D
@Gt2True
D;JGT
// set false to D
D=0
@Gt2End
0;JMP
(Gt2True)
// set true to D
D=-1
(Gt2End)
// set result to the stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// -----------------------
// constant to D
@32766
D=A
// push D to stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// constant to D
@32766
D=A
// push D to stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// gt
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
// calculate on the stack
D=M-D
@Gt3True
D;JGT
// set false to D
D=0
@Gt3End
0;JMP
(Gt3True)
// set true to D
D=-1
(Gt3End)
// set result to the stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// -----------------------
// constant to D
@57
D=A
// push D to stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// constant to D
@31
D=A
// push D to stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// constant to D
@53
D=A
// push D to stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// add
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
// calculate on the stack
M=D+M
// increment stack pointer
@SP
M=M+1
// -----------------------
// constant to D
@112
D=A
// push D to stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// sub
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
// calculate on the stack
M=M-D
// increment stack pointer
@SP
M=M+1
// -----------------------
// neg
// decrement stack pointer
@SP
M=M-1
A=M
// calculate on the stack
M=-M
// increment stack pointer
@SP
M=M+1
// -----------------------
// and
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
// calculate on the stack
M=D&M
// increment stack pointer
@SP
M=M+1
// -----------------------
// constant to D
@82
D=A
// push D to stack
@SP
A=M
M=D
// increment stack pointer
@SP
M=M+1
// or
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
// calculate on the stack
M=D|M
// increment stack pointer
@SP
M=M+1
// -----------------------
// not
// decrement stack pointer
@SP
M=M-1
A=M
// calculate on the stack
M=!M
// increment stack pointer
@SP
M=M+1
// -----------------------
