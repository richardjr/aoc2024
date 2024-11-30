org $8000   ; Start address of the program
    ld hl,MESSAGE
    call PRINT_STRING
    call NEWLINE
    ret

PRINT_STRING:
    ld a,(hl)       ; Load the byte at the address in HL into A.
    cp 255           ; Set the zero flag if A is zero.
    ret z           ; Return if A is zero.
    inc hl          ; Increment HL.
    call PRINT_CHAR ; Print the character in A.
    jr PRINT_STRING ; Jump back to print the next character.

PRINT_CHAR:
    push hl
    ld b,a          ; Copy the character to B.
    ld a,2           ; Set the output function to 2.
    call &1601
    ld a,b          ; Restore the character to A.
    rst &0010           ; Call the ROM routine to print the character.
    pop hl
    ret

NEWLINE:
    ld a,13          ; Load the ASCII code for a newline into A.
    jr PRINT_CHAR  ; Print the newline character.
    ret

CLEAR_SCREEN:
    ld a,110         ; Yellow ink (6), cyan paper (5 * 8), bright (64).
    ld (23693),a    ; Set our screen colours.
    ld a,5           ; Load accumulator with zero.
    call 8859       ; Set permanent border colours.
    call 3503       ; Clear the screen, open channel 2.
    ret

MESSAGE: db "Hello, World!", 255

end $8000
