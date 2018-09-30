// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

(Loop)
    // Select color by keyboard
    @KBD
    D=M
    @FillScreen
    D;JEQ
    D=-1
(FillScreen)
	@color // Set color from D register
	M=D
	// Set screen address to @pos
    @SCREEN
    D=A
    @8192
    D=D+A
    @pos
    M=D
(Fillloop)
    @pos
    D=M-1
    M=D

	@SCREEN
	D=D-A
	@Loop
	D;JLT

    // Set color to D
    @color
    D=M

    // Fill color to @pos
    @pos
    A=M
    M=D
	@Fillloop
    0;JMP
