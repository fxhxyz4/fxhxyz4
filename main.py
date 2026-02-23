import gifos

from config import (
    USER, HOSTNAME,
    BIRTH_DAY, BIRTH_MONTH, BIRTH_YEAR,
    DISTRO_NAME, KERNEL, SHELL, DE_WM, TERMINAL_APP, EDITOR,
    HOST_MACHINE, CPU, GPU, MEMORY,
    GITHUB_URL, TELEGRAM_URL,
    TERMINAL_WIDTH, TERMINAL_HEIGHT, FPS,
    FONT_MAIN, FONT_SIZE,
)

RESET = "\x1b[0m"
BOLD  = "\x1b[1m"
DIM   = "\x1b[2m"

BLACK  = "\x1b[30m"; RED    = "\x1b[31m"; GREEN  = "\x1b[32m"; YELLOW = "\x1b[33m"
BLUE   = "\x1b[34m"; MAG    = "\x1b[35m"; CYAN   = "\x1b[36m"; WHITE  = "\x1b[37m"
BBLACK = "\x1b[90m"; BRED   = "\x1b[91m"; BGREEN = "\x1b[92m"; BYELL  = "\x1b[93m"
BBLUE  = "\x1b[94m"; BMAG   = "\x1b[95m"; BCYAN  = "\x1b[96m"; BWHITE = "\x1b[97m"

C_USER  = BYELL
C_AT    = BWHITE
C_HOST  = BCYAN
C_KEY   = BCYAN
C_VAL   = BWHITE
C_MUTED = BBLACK
C_LINK  = BBLUE
C_LOGO1 = BBLUE
C_LOGO2 = BLUE
C_CMD   = BCYAN
C_FLAG  = BWHITE
C_ARG   = BYELL

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
    "        .oossssso-````/ossssss+`         ",
    "       -osssssso.      :ssssssso.        ",
    "      :osssssss/        osssso+++.       ",
    "     /ossssssss/        +ssssooo/-       ",
    "   `/ossssso+/:-        -:/+osssso+-     ",
    "  `+sso+:-`                 `.-/+oso:    ",
    " `++:.                           `-/+/   ",
    " .`                                 `     ",
]

def colorize_logo(lines):
    out = []
    split = len(lines) // 2
    for i, s in enumerate(lines):
        c = C_LOGO1 if i < split else C_LOGO2
        out.append(c + s + RESET)
    return out

ARCH_LOGO = colorize_logo(ARCH_LOGO_RAW)

def visible_len(s):
    esc = False
    n = 0
    for ch in s:
        if ch == "\x1b":
            esc = True
        elif not esc:
            n += 1
        if esc and ch == "m":
            esc = False
    return n

def build_info_lines(age):
    key_w = 7

    def kv(key, val, vcol=C_VAL):
        return f"{C_KEY}{key:<{key_w}}{RESET} {vcol}{val}{RESET}"

    sep = f"{C_MUTED}{'-' * 30}{RESET}"

    header = (
        f"{BOLD}{C_USER}{USER}{RESET}"
        f"{C_AT}@{RESET}"
        f"{BOLD}{C_HOST}{HOSTNAME}{RESET}"
    )

    lines = [
        header,
        sep,
        kv("distro",  DISTRO_NAME),
        kv("kernel",  KERNEL),
        kv("shell",   SHELL),
        kv("wm",      DE_WM),
        kv("term",    TERMINAL_APP),
        kv("editor",  EDITOR),
        sep,
        kv("host",    HOST_MACHINE),
        kv("cpu",     CPU),
        kv("gpu",     GPU),
        kv("memory",  f"{MEMORY} DDR4-3200 SO-DIMM"),
        f"{C_MUTED}{'':<{key_w}}{RESET}",
        sep,
        kv("age",     f"{age.years}y {age.months}m {age.days}d"),
    ]

    if GITHUB_URL:
        lines.append(kv("github", GITHUB_URL, vcol=C_LINK))
    if TELEGRAM_URL:
        lines.append(kv("tg", TELEGRAM_URL, vcol=C_LINK))

    return lines

def make_palette_ultra_safe():
    cols = [RED, GREEN, YELLOW, BLUE, MAG, CYAN, WHITE, BBLACK]
    blocks = "".join(c + "##" + RESET for c in cols)
    return f"{C_MUTED}colors{RESET} {blocks}"

def main():
    t = gifos.Terminal(TERMINAL_WIDTH, TERMINAL_HEIGHT, 15, 15, FONT_MAIN, FONT_SIZE)
    t.set_fps(FPS)

    prompt = (
        f"{C_LOGO1}{USER}{RESET}"
        f"{C_AT}@{RESET}"
        f"{C_HOST}{HOSTNAME}{RESET} "
        f"{DIM}~{RESET} "
    )
    cmd = f"{C_CMD}fetch.sh{RESET} {C_FLAG}-u{RESET} {C_ARG}fxhxyz{RESET}"

    t.toggle_show_cursor(False)
    t.gen_text(prompt, 1, 2, count=10, contin=True)
    t.toggle_show_cursor(True)
    t.gen_typing_text(cmd, 1, 2 + visible_len(prompt), contin=True)
    t.toggle_show_cursor(False)

    t.gen_text("", 2, 2, count=FPS * 1, contin=True)

    age = gifos.utils.calc_age(BIRTH_DAY, BIRTH_MONTH, BIRTH_YEAR)
    info = build_info_lines(age)

    LOGO_ROW = 3
    LOGO_COL = 2
    INFO_COL = LOGO_COL + max(len(s) for s in ARCH_LOGO_RAW) + 3

    for i, line in enumerate(ARCH_LOGO):
        t.gen_text(line, LOGO_ROW + i, LOGO_COL, count=2, contin=True)

    for i, line in enumerate(info):
        t.gen_text(line, LOGO_ROW + i, INFO_COL, count=2, contin=True)

    palette_row = LOGO_ROW + max(len(ARCH_LOGO), len(info)) + 1
    t.gen_text(make_palette_ultra_safe(), palette_row, INFO_COL, count=4, contin=True)

    footer_row = palette_row + 2
    t.gen_text("", footer_row + 1, 2, count=FPS * 5, contin=True)

    t.toggle_show_cursor(True)
    t.gen_gif()
    print("✓ output.gif saved")

if __name__ == "__main__":
    main()