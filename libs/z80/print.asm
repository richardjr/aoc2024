;; This file contains routines to print strings and characters to the screen.
;; It is designed to be used with the ZX Spectrum 48K.

;; Colour attributes for the ZX Spectrum 48K.
;; The screen is 32x24 characters, with each character being 8x8 pixels.
;; The screen memory is 6144 bytes long, with each byte representing the

BLACK: db $00
BLUE: DB $01
RED: DB $02
MAGENTA: DB $03
GREEN: DB $04
CYAN: DB $05
YELLOW: DB $06
WHITE: DB $07

;; SET_BORDER sets the border colour of the screen.
;; A = border colour (0-7).
SET_BORDER:
    ld c, 143
    out  (PORT_BORDER), a
    ret

;; Load HL with the address of the string to print and call PRINT_STRING.

PRINT_STRING:
    ld a,(hl)       ; Load the byte at the address in HL into A.
    cp 255           ; Set the zero flag if A is zero.
    ret z           ; Return if A is zero.
    inc hl          ; Increment HL.
    call PRINT_CHAR ; Print the character in A.
    jr PRINT_STRING ; Jump back to print the next character.


;; Pint an array of 16-bit integers.
;; HL = address of the array.
;; B = number of elements in the array.
PRINT_ARRAY_16:
    ld a,(hl)       ; Load the low byte of the first element into A.
    ld d,a        ; Copy the low byte to DE.
    inc hl          ; Increment HL to point to the high byte.
    ld a,(hl)       ; Load the high byte of the first element into A.
    ld e,a        ; Copy the low byte to DE.
    call $2033
    inc hl          ; Increment HL to point to the high byte.
    dec b           ; Decrement B.
    ld a,b          ; Copy B to A.
    cp 0            ; Set the zero flag if B is zero.
    ret z           ; Return if B is zero.
    jr PRINT_ARRAY_16

;; Load A with the ASCII code of the character to print and call PRINT_CHAR.

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
    call CLS
    ret

;; LOCATE_X_Y sets the cursor position on the screen.
;; A = X position (0-31).
;; B = Y position (0-23).
LOCATE_X_Y:
    call LOCATE
    ret

