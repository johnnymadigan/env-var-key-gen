from src.constants.consts import API_KEYS_FILE_NAME, KV_PAIRS_FILE_NAME
from src.utils.string_utils import mask_string
from functools import wraps
import csv
import os


def _format_csv_file_name(file_name: str) -> str:
    """Adds .csv extension to the file name"""
    EXTENSION = ".csv"
    res = file_name if file_name.endswith(EXTENSION) else file_name + EXTENSION
    return res


def ensure_csv_exist(func):
    """
    DECORATOR: Ensures vital CSV files exist
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        for file in [API_KEYS_FILE_NAME, KV_PAIRS_FILE_NAME]:
            full_name = _format_csv_file_name(file)
            if not os.path.exists(full_name):
                open(full_name, "a").close
        return func(*args, **kwargs)

    return wrapper


@ensure_csv_exist
def get_csv_rows(file_name: str) -> list[list[str]]:
    """
    Returns a list of rows for any CSV file
    """
    full_name = _format_csv_file_name(file_name)
    rows = []

    with open(full_name, newline="") as csv_file:
        reader = csv.reader(csv_file)
        rows = [row for row in reader]

    return rows


@ensure_csv_exist
def add_key(value: str, key: str) -> None:
    """
    - Adds the new key to the keys CSV file
    - Adds a relationship row between the value and key in the KV pairs CSV file
    - Throws if value already exists
    """
    api_keys_file_name = _format_csv_file_name(API_KEYS_FILE_NAME)
    kv_pairs_file_name = _format_csv_file_name(KV_PAIRS_FILE_NAME)
    masked_key = mask_string(key)
    existing_pair_values = [row[1] for row in get_csv_rows(kv_pairs_file_name)]

    # Confirm value not taken
    if value in existing_pair_values:
        raise ValueError(f"Key already exists for {value}")

    try:
        with open(api_keys_file_name, "a", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([key])

        with open(kv_pairs_file_name, "a", newline="") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([masked_key, value])
    except Exception as e:
        print(f"error: {e}")


@ensure_csv_exist
def remove_key(target_key: str) -> None:
    """
    Removes an API key from the CSV if it exists
    """
    file_name = _format_csv_file_name(API_KEYS_FILE_NAME)
    existing_keys = [row[0] for row in get_csv_rows(file_name)]

    # Re-write w/o target key if it exists
    if target_key in existing_keys:
        with open(file_name, "w", newline="") as csv_file:
            writer = csv.writer(csv_file)
            for key in existing_keys:
                if key == target_key:
                    continue
                writer.writerow([key])


@ensure_csv_exist
def remove_pair(target_value: str) -> None:
    """
    Removes a KV pair from the CSV if it exists
    """
    file_name = _format_csv_file_name(KV_PAIRS_FILE_NAME)
    existing_pairs = get_csv_rows(file_name)

    with open(file_name, "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        for pair in existing_pairs:
            if pair[1] == target_value:
                continue
            writer.writerow(pair)
