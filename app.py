#!venv/bin/python

from src.main import cli

if __name__ == "__main__":
    try:
        cli()
    except Exception as ex:
        print(f"Command failed: {ex}")
