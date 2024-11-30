
org $8000   ; Start address of the program
    ld a,(CYAN)
    call SET_BORDER
    call CLEAR_SCREEN
    ld a,8
    ld b,5
    call LOCATE_X_Y
    ld hl,MESSAGE
    call PRINT_STRING
    call NEWLINE
    ret

include "../../libs/z80/rom.asm"
include "../../libs/z80/ports.asm"
include "../../libs/z80/print.asm"

MESSAGE: db "AOC 2024 Spectrum 48k", 255

end $8000
