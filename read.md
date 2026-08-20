# GitHub Terminal

Animated retro terminal GIF for a GitHub profile README.

This project generates a terminal-style animation with an Arch Linux system
summary, hardware information, links, and a live age counter.

## 🚀 Local setup

Python 3.10+ is recommended.

```bash
source .venv/bin/activate
pip install --upgrade "Pillow>=11.0.0"
pip install --no-deps github-readme-terminal
pip install icecream python-dateutil python-dotenv requests tomli

python main.py
```

The generated animation is saved as `output.gif`.

## ⚙️ Configuration

Most customization is intentionally kept in `config.py`.

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

Required repository secrets:

- `GH_TOKEN`
- `IMGBB_API_KEY`

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
