from src.constants.consts import API_KEYS_FILE_NAME, KV_PAIRS_FILE_NAME, OUTPUT_DIR
from src.utils.csv_utils import ensure_csv_extension
from functools import wraps
import os


def ensure_files_exist(func):
    """
    DECORATOR:
        - Ensures vital files exist and their relative directory
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        os.makedirs(OUTPUT_DIR, exist_ok=True)

        files = [API_KEYS_FILE_NAME, KV_PAIRS_FILE_NAME]

        for file in files:
            csv = f"{OUTPUT_DIR}/{ensure_csv_extension(file)}"
            if not os.path.exists(csv):
                with open(csv, "a"):
                    pass
        return func(*args, **kwargs)

    return wrapper
