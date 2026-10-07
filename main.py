import os
from pathlib import Path

os.chdir(Path(__file__).resolve().parent)

from modules.renderer import render

if __name__ == "__main__":
    render()
