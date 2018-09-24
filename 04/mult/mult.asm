// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Set R2 to 0
    @R2
    M=0
(Start)
    // Load R0
    @R0
    D=M

    // End if R0=0
    @End
    D;JEQ

    // R2 += R1
    @R1
    D=M
    @R2
    M=D+M

    // R0 -= 1
    @R0
    M=M-1
    @Start
    0;JMP
(End)
    @End
    0;JMP
