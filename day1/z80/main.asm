
org $8000   ; Start address of the program
    ld a,(CYAN)
    call SET_BORDER
    call CLEAR_SCREEN
    ld hl,MESSAGE
    call PRINT_STRING
    call NEWLINE
    ld b,ARRAY1LEN
    ld hl,ARRAY1
    call PRINT_ARRAY_16
    ret



include "../../libs/z80/rom.asm"
include "../../libs/z80/ports.asm"
include "../../libs/z80/print.asm"
include "data.asm"
MESSAGE: db "AOC 2024 48k Day One A", 255

end $8000
