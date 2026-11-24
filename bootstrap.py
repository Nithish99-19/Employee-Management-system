"""One command setup: creates .venv, installs requirements, then runs run.py.

Usage:  python bootstrap.py
"""
import os
import subprocess
import sys
import venv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VENV = ROOT / ".venv"


def venv_python():
    if os.name == "nt":
        return VENV / "Scripts" / "python.exe"
    return VENV / "bin" / "python"


def main():
    if not venv_python().exists():
        print("Creating virtual environment in .venv ...")
        venv.create(VENV, with_pip=True)
    py = str(venv_python())
    print("Installing requirements ...")
    subprocess.check_call([py, "-m", "pip", "install", "-q", "-r", str(ROOT / "requirements.txt")])
    print("Starting the app ...")
    subprocess.check_call([py, str(ROOT / "run.py")], cwd=ROOT)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
