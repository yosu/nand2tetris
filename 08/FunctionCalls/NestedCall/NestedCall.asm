// ------------------------------------------------------------------------------
//init
// ------------------------------------------------------------------------------
@Function.Sys.init
0;JMP
// ------------------------------------------------------------------------------
// function Sys.init 0
// ------------------------------------------------------------------------------
(Function.Sys.init)
// ------------------------------------------------------------------------------
// push constant 4000
// ------------------------------------------------------------------------------
@4000
D=A
@SP
A=M
M=D
@SP
M=M+1
// ------------------------------------------------------------------------------
// pop pointer 0
// ------------------------------------------------------------------------------
@THIS
D=A
@0
D=D+A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// ------------------------------------------------------------------------------
// push constant 5000
// ------------------------------------------------------------------------------
@5000
D=A
@SP
A=M
M=D
@SP
M=M+1
// ------------------------------------------------------------------------------
// pop pointer 1
// ------------------------------------------------------------------------------
@THIS
D=A
@1
D=D+A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// ------------------------------------------------------------------------------
// call Sys.main 0
// ------------------------------------------------------------------------------
@Return.Sys.1
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@5
D=D+A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Function.Sys.main
0;JMP
(Return.Sys.1)
// ------------------------------------------------------------------------------
// pop temp 1
// ------------------------------------------------------------------------------
@R5
D=A
@1
D=D+A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// ------------------------------------------------------------------------------
// label LOOP
// ------------------------------------------------------------------------------
(LabelLOOP)
// ------------------------------------------------------------------------------
// goto LOOP
// ------------------------------------------------------------------------------
@LabelLOOP
0;JMP
// ------------------------------------------------------------------------------
// function Sys.main 5
// ------------------------------------------------------------------------------
(Function.Sys.main)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// ------------------------------------------------------------------------------
// push constant 4001
// ------------------------------------------------------------------------------
@4001
D=A
@SP
A=M
M=D
@SP
M=M+1
// ------------------------------------------------------------------------------
// pop pointer 0
// ------------------------------------------------------------------------------
@THIS
D=A
@0
D=D+A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// ------------------------------------------------------------------------------
// push constant 5001
// ------------------------------------------------------------------------------
@5001
D=A
@SP
A=M
M=D
@SP
M=M+1
// ------------------------------------------------------------------------------
// pop pointer 1
// ------------------------------------------------------------------------------
@THIS
D=A
@1
D=D+A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// ------------------------------------------------------------------------------
// push constant 200
// ------------------------------------------------------------------------------
@200
D=A
@SP
A=M
M=D
@SP
M=M+1
// ------------------------------------------------------------------------------
// pop local 1
// ------------------------------------------------------------------------------
@LCL
D=M
@1
D=D+A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// ------------------------------------------------------------------------------
// push constant 40
// ------------------------------------------------------------------------------
@40
D=A
@SP
A=M
M=D
@SP
M=M+1
// ------------------------------------------------------------------------------
// pop local 2
// ------------------------------------------------------------------------------
@LCL
D=M
@2
D=D+A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// ------------------------------------------------------------------------------
// push constant 6
// ------------------------------------------------------------------------------
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
// ------------------------------------------------------------------------------
// pop local 3
// ------------------------------------------------------------------------------
@LCL
D=M
@3
D=D+A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// ------------------------------------------------------------------------------
// push constant 123
// ------------------------------------------------------------------------------
@123
D=A
@SP
A=M
M=D
@SP
M=M+1
// ------------------------------------------------------------------------------
// call Sys.add12 1
// ------------------------------------------------------------------------------
@Return.Sys.2
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@1
D=A
@5
D=D+A
@SP
D=M-D
@ARG
M=D
@SP
D=M
@LCL
M=D
@Function.Sys.add12
0;JMP
(Return.Sys.2)
// ------------------------------------------------------------------------------
// pop temp 0
// ------------------------------------------------------------------------------
@R5
D=A
@0
D=D+A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// ------------------------------------------------------------------------------
// push local 0
// ------------------------------------------------------------------------------
@LCL
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
// ------------------------------------------------------------------------------
// push local 1
// ------------------------------------------------------------------------------
@LCL
D=M
@1
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
// ------------------------------------------------------------------------------
// push local 2
// ------------------------------------------------------------------------------
@LCL
D=M
@2
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
// ------------------------------------------------------------------------------
// push local 3
// ------------------------------------------------------------------------------
@LCL
D=M
@3
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
// ------------------------------------------------------------------------------
// push local 4
// ------------------------------------------------------------------------------
@LCL
D=M
@4
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
// ------------------------------------------------------------------------------
// add
// ------------------------------------------------------------------------------
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=D+M
@SP
M=M+1
// ------------------------------------------------------------------------------
// add
// ------------------------------------------------------------------------------
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=D+M
@SP
M=M+1
// ------------------------------------------------------------------------------
// add
// ------------------------------------------------------------------------------
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=D+M
@SP
M=M+1
// ------------------------------------------------------------------------------
// add
// ------------------------------------------------------------------------------
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=D+M
@SP
M=M+1
// ------------------------------------------------------------------------------
// return
// ------------------------------------------------------------------------------
@LCL
D=M
@R13
M=D
@5
A=D-A
D=M
@R14
M=D
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@R13
M=M-1
A=M
D=M
@THAT
M=D
@R13
M=M-1
A=M
D=M
@THIS
M=D
@R13
M=M-1
A=M
D=M
@ARG
M=D
@R13
M=M-1
A=M
D=M
@LCL
M=D
@R14
A=M
0;JMP
// ------------------------------------------------------------------------------
// function Sys.add12 0
// ------------------------------------------------------------------------------
(Function.Sys.add12)
// ------------------------------------------------------------------------------
// push constant 4002
// ------------------------------------------------------------------------------
@4002
D=A
@SP
A=M
M=D
@SP
M=M+1
// ------------------------------------------------------------------------------
// pop pointer 0
// ------------------------------------------------------------------------------
@THIS
D=A
@0
D=D+A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// ------------------------------------------------------------------------------
// push constant 5002
// ------------------------------------------------------------------------------
@5002
D=A
@SP
A=M
M=D
@SP
M=M+1
// ------------------------------------------------------------------------------
// pop pointer 1
// ------------------------------------------------------------------------------
@THIS
D=A
@1
D=D+A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// ------------------------------------------------------------------------------
// push argument 0
// ------------------------------------------------------------------------------
@ARG
D=M
@0
A=D+A
D=M
@SP
A=M
M=D
@SP
M=M+1
// ------------------------------------------------------------------------------
// push constant 12
// ------------------------------------------------------------------------------
@12
D=A
@SP
A=M
M=D
@SP
M=M+1
// ------------------------------------------------------------------------------
// add
// ------------------------------------------------------------------------------
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=D+M
@SP
M=M+1
// ------------------------------------------------------------------------------
// return
// ------------------------------------------------------------------------------
@LCL
D=M
@R13
M=D
@5
A=D-A
D=M
@R14
M=D
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
@ARG
D=M+1
@SP
M=D
@R13
M=M-1
A=M
D=M
@THAT
M=D
@R13
M=M-1
A=M
D=M
@THIS
M=D
@R13
M=M-1
A=M
D=M
@ARG
M=D
@R13
M=M-1
A=M
D=M
@LCL
M=D
@R14
A=M
0;JMP