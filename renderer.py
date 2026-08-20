from pathlib import Path

import gifos

from config import (
    BIRTH_DAY, BIRTH_MONTH, BIRTH_YEAR,
    TERMINAL_WIDTH, TERMINAL_HEIGHT, FPS,
    FONT_MAIN, FONT_SIZE,
    USER, HOSTNAME, GITHUB_USER,
    DISTRO_NAME, KERNEL, SHELL, DE_WM, TERMINAL_APP, EDITOR,
    HOST_MACHINE, CPU, GPU, MEMORY,
    GITHUB_URL, TELEGRAM_URL,
)
from terminal_info import SystemInfo, build_info_lines
from terminal_logo import ARCH_LOGO, ARCH_LOGO_RAW
from terminal_theme import RESET, DIM, AT, HOST, LOGO_PRIMARY, COMMAND, FLAG, ARGUMENT
from terminal_utils import make_palette, visible_len

def build_system_info() -> SystemInfo:
    return SystemInfo(
        user=USER,
        hostname=HOSTNAME,
        distro=DISTRO_NAME,
        kernel=KERNEL,
        shell=SHELL,
        wm=DE_WM,
        terminal=TERMINAL_APP,
        editor=EDITOR,
        host=HOST_MACHINE,
        cpu=CPU,
        gpu=GPU,
        memory=MEMORY,
        github_url=GITHUB_URL,
        telegram_url=TELEGRAM_URL,
    )

def render(output: str = "output.gif") -> None:
    terminal = gifos.Terminal(
        TERMINAL_WIDTH,
        TERMINAL_HEIGHT,
        15,
        15,
        FONT_MAIN,
        FONT_SIZE,
    )
    terminal.set_fps(FPS)

    prompt = (
        f"{LOGO_PRIMARY}{USER}{RESET}"
        f"{AT}@{RESET}"
        f"{HOST}{HOSTNAME}{RESET} "
        f"{DIM}~{RESET} "
    )
    command = (
        f"{COMMAND}fetch.sh{RESET} "
        f"{FLAG}-u{RESET} "
        f"{ARGUMENT}{GITHUB_USER}{RESET}"
    )

    terminal.toggle_show_cursor(False)
    terminal.gen_text(prompt, 1, 2, count=10, contin=True)
    terminal.toggle_show_cursor(True)
    terminal.gen_typing_text(
        command,
        1,
        2 + visible_len(prompt),
        contin=True,
    )
    terminal.toggle_show_cursor(False)

    terminal.gen_text("", 2, 2, count=FPS, contin=True)

    age = gifos.utils.calc_age(BIRTH_DAY, BIRTH_MONTH, BIRTH_YEAR)
    info = build_info_lines(build_system_info(), age)

    logo_row = 3
    logo_col = 2
    info_col = logo_col + max(map(len, ARCH_LOGO_RAW)) + 3

    for index, line in enumerate(ARCH_LOGO):
        terminal.gen_text(line, logo_row + index, logo_col, count=2, contin=True)

    for index, line in enumerate(info):
        terminal.gen_text(line, logo_row + index, info_col, count=2, contin=True)

    palette_row = logo_row + max(len(ARCH_LOGO), len(info)) + 1
    terminal.gen_text(make_palette(), palette_row, info_col, count=4, contin=True)

    terminal.gen_text(
        "",
        palette_row + 3,
        2,
        count=FPS * 5,
        contin=True,
    )

    terminal.toggle_show_cursor(True)
    terminal.gen_gif()

    generated = Path("output.gif")
    if output != str(generated):
        generated.replace(output)

    print(f"✓ {output} saved")
