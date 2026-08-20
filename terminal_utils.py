import re

ANSI_ESCAPE_RE = re.compile(r"\x1b\[[0-?]*[ -/]*[@-~]")

def visible_len(text: str) -> int:
    return len(ANSI_ESCAPE_RE.sub("", text))

def make_palette() -> str:
    from terminal_theme import (
        RESET, MUTED, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE,
        BRIGHT_BLACK,
    )

    colors = [RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, BRIGHT_BLACK]
    blocks = "".join(f"{color}##{RESET}" for color in colors)
    return f"{MUTED}colors{RESET} {blocks}"
