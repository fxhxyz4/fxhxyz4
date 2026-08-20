from terminal_theme import RESET, LOGO_PRIMARY, LOGO_SECONDARY

ARCH_LOGO_RAW = [
    "                   -`                    ",
    "                  .o+`                   ",
    "                 `ooo/                   ",
    "                `+oooo:                  ",
    "               `+oooooo:                 ",
    "               -+oooooo+:                ",
    "             `/:-:++oooo+:               ",
    "            `/++++/+++++++:              ",
    "           `/++++++++++++++:             ",
    "          `/+++ooooooooooooo/`           ",
    "         ./ooosssso++osssssso+`          ",
    "        .oossssso-````/osssssso+`         ",
    "       -osssssso.      :ssssssso.        ",
    "      :osssssss/        osssso+++.       ",
    "     /ossssssss/        +ssssooo/-       ",
    "   `/ossssso+/:-        -:/+osssso+-     ",
    "  `+sso+:-`                 `.-/+oso:    ",
    " `++:.                           `-/+/   ",
    " .`                                 `     ",
]

def colorize_logo(lines: list[str]) -> list[str]:
    split = len(lines) // 2
    return [
        f"{LOGO_PRIMARY if i < split else LOGO_SECONDARY}{line}{RESET}"
        for i, line in enumerate(lines)
    ]


ARCH_LOGO = colorize_logo(ARCH_LOGO_RAW)
