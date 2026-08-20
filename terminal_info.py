from dataclasses import dataclass

from terminal_theme import (
    RESET, BOLD, AT, HOST, KEY, VALUE, MUTED, LINK, USER,
)

@dataclass(frozen=True)
class SystemInfo:
    user: str
    hostname: str
    distro: str
    kernel: str
    shell: str
    wm: str
    terminal: str
    editor: str
    host: str
    cpu: str
    gpu: str
    memory: str
    github_url: str = ""
    telegram_url: str = ""

def build_info_lines(info: SystemInfo, age) -> list[str]:
    key_width = 7

    def kv(key: str, value: str, value_color: str = VALUE) -> str:
        return f"{KEY}{key:<{key_width}}{RESET} {value_color}{value}{RESET}"

    separator = f"{MUTED}{'-' * 30}{RESET}"
    header = (
        f"{BOLD}{USER}{info.user}{RESET}"
        f"{AT}@{RESET}"
        f"{BOLD}{HOST}{info.hostname}{RESET}"
    )

    lines = [
        header,
        separator,
        kv("distro", info.distro),
        kv("kernel", info.kernel),
        kv("shell", info.shell),
        kv("wm", info.wm),
        kv("term", info.terminal),
        kv("editor", info.editor),
        separator,
        kv("host", info.host),
        kv("cpu", info.cpu),
        kv("gpu", info.gpu),
        kv("memory", f"{info.memory} DDR4-3200 SO-DIMM"),
        f"{MUTED}{'':<{key_width}}{RESET}",
        separator,
        kv("age", f"{age.years}y {age.months}m {age.days}d"),
    ]

    if info.github_url:
        lines.append(kv("github", info.github_url, value_color=LINK))
    if info.telegram_url:
        lines.append(kv("tg", info.telegram_url, value_color=LINK))

    return lines
