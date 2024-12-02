
org $8000   ; Start address of the program
    ld a,(CYAN)
    call SET_BORDER
    call CLEAR_SCREEN
    ld hl,MESSAGE
    call PRINT_STRING
    call NEWLINE
    ld hl,ARRAY
    call MAIN
    ld hl,MESSAGE3
    call PRINT_STRING
    ret

MAIN:
    ;; Print a dot
    ;;ld a, 46
    ;;call PRINT_CHAR
    ld a, 0
    ld (SAFE), a
    ld a, (hl)
    cp 254 ; Set the zero flag if A is zero.
    ret z ; Return if A is zero.
    inc hl ; skip the first byte
LOOP1:
    ld a, (hl)
    cp 255 ; Set the zero flag if A is 255.
    jr nz, CONTINUE1
    inc hl
    ;; check safe
    ld a, (SAFE)
    cp 0
    jr nz, MAIN
    ld a, (COUNT)
    inc a
    ld (COUNT), a
    jr MAIN
CONTINUE1:
    ld a,(CHARS)
    inc a
    ld (CHARS), a
DIFF3:
    ; Check if the absolute difference between current and previous value is less than 3

    ld a, (hl)
    ld b, a
    dec hl
    ld a, (hl)
    inc hl
    ld c, a            ; Save previous value in C
    ld a, b            ; A = current value
    sub c              ; A = A - C (current - previous)

    ; Get absolute value of the difference
    ld e, a            ; Save the result in E
    bit 7, a           ; Check if the result is negative (sign flag set)
    jr z, POSITIVE_DIFF
    ; If negative,  get abs
    cpl                ; Complement A (one's complement)
    inc a              ; Add 1 to complete two's complement (A = -A)
POSITIVE_DIFF:
    ; Compare the absolute difference to 4
    cp 4               ; Compare A to 4
    jr c, DIFF4        ; If A <= 3, jump to DIFF4

    ; Absolute difference >= 3, continue processing
    inc hl             ; Move HL to next value
    jr LOOP1

DIFF4:
    ; Absolute difference <= 3, set SAFE to 1
    ld a, 1
    ld (SAFE), a
    inc hl             ; Move HL to next value
    jr LOOP1

include "../../libs/z80/rom.asm"
include "../../libs/z80/ports.asm"
include "../../libs/z80/print.asm"
include "data.asm"
MESSAGE: db "AOC 2024 48k Day Two A", 255
MESSAGE2: db "Processing Line", 255
MESSAGE3: db "Done", 255

COUNT: db 0
CHARS: db 0
SAFE: db 0

end $8000
