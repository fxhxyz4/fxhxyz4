# GitHub Terminal

Animated retro terminal GIF for a GitHub profile README.

This project generates a terminal-style animation with an Arch Linux system
summary, hardware information, links, and a live age counter.

## 🚀 Local setup

Requires Python 3.10+ and FFmpeg installed on your system.

```bash
python -m venv .venv
source .venv/bin/activate

python -m pip install -r requirements.txt
python -m pip install --no-deps -r nodeps.txt

python main.py
```

The generated animation is saved as `output.gif`.

## ⚙️ Configuration

Most customization is intentionally kept in `./config/cfg.py`.

You can change:

- username and hostname
- birth date
- Linux distribution and kernel
- shell, WM, terminal, and editor
- hardware information
- GitHub and Telegram links
- GIF dimensions and FPS
- font and font size

No renderer code should need to be changed for normal profile customization.

## 🤖 GitHub Actions

The included workflow can regenerate `output.gif` on demand or on a schedule.

The workflow installs the `github-readme-terminal` package and uses the same
`gifos` rendering stack as the local project.

## 💡 Original idea

This project is based on the idea of using an animated retro terminal in a
GitHub profile README.

Original project and inspiration:

**[x0rzavi/github-readme-terminal](https://github.com/x0rzavi/github-readme-terminal)**

The original repository is MIT licensed. This project keeps the inspiration
credit here intentionally.

## 📄 License

MIT. See the original repository for the upstream project and its license.
