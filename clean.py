from pathlib import Path
from config.config import BASE_DIR


def clear():
    target_folder = Path(BASE_DIR / "uploads")
    files = target_folder.glob("*.*")
    for file in files:
        try:
            file.unlink()
        except FileNotFoundError as err:
            print(err)
    print(f'Files in {target_folder} was deleted!')


if __name__ == "__main__":
    clear()
