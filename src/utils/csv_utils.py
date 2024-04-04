from src.constants.consts import API_KEYS_FILE_NAME, KV_PAIRS_FILE_NAME, OUTPUT_DIR
from src.utils.string_utils import mask_string
from src.utils.key_utils import generate_key
import fnmatch
import csv
import os

# INVARIANTS:
#   - All seed values are converted to lowercase

def ensure_csv_extension(file_name: str) -> str:
    return file_name if file_name.endswith(".csv") else file_name + ".csv"


def get_csv_rows(file_name: str) -> list[list[str]]:
    """Returns a list of rows for any CSV file"""
    csv_name = ensure_csv_extension(file_name)

    # Guard: file not found
    if not os.path.exists(csv_name):
        raise FileNotFoundError(f"File '{csv_name}' not found")

    with open(csv_name, newline="") as csv_file:
        return [row for row in csv.reader(csv_file)]

def delete_csv() -> None:
    for file in os.listdir(OUTPUT_DIR):
        if fnmatch.fnmatch(file, "*.csv"):
            csv_file = os.path.join(OUTPUT_DIR, file)
            os.remove(csv_file)

def add_key(seed_value: str) -> str:
    """
    - Generates a new key based on the value
    - Adds the new key to 'Keys' CSV
    - Adds a relationship record between the Value and Key in 'KV Pairs' CSV
    - Throws if value already exists
    """
    # Gen and format new values
    seed_value_formatted = seed_value.lower()
    key = generate_key(seed_value_formatted)

    api_keys_csv_name = ensure_csv_extension(os.path.join(OUTPUT_DIR, API_KEYS_FILE_NAME))
    kv_pairs_csv_name = ensure_csv_extension(os.path.join(OUTPUT_DIR, KV_PAIRS_FILE_NAME))

    existing_pair_values = [row[1] for row in get_csv_rows(kv_pairs_csv_name)]

    # Guard: confirm value not taken
    if seed_value_formatted in existing_pair_values:
        raise ValueError(f"Key already exists for {seed_value}")

    with open(api_keys_csv_name, "a", newline="") as csv_file:
        csv.writer(csv_file).writerow([key])

    with open(kv_pairs_csv_name, "a", newline="") as csv_file:
        csv.writer(csv_file).writerow([mask_string(key), seed_value_formatted])

    return key


def remove_key_for_value(value: str) -> None:
    """
    - Removes an API key from 'Keys' CSV if it exists
    - Always syncs this change in 'KV Pairs' CSV
    - Throws if key already deleted from 'Keys' CSV
    """
    # Gen and format values to remove
    value_formatted = value.lower()
    target_key = generate_key(value_formatted)

    file_name = ensure_csv_extension(os.path.join(OUTPUT_DIR, API_KEYS_FILE_NAME))

    existing_keys = [row[0] for row in get_csv_rows(file_name)]

    # Guard: ensure value not already deleted
    _remove_pair(value_formatted) # sync

    if target_key not in existing_keys:
        raise ValueError(f"Key already deleted for {value}")
    
    with open(file_name, "w", newline="") as csv_file:
        csv.writer(csv_file).writerows([[key] for key in existing_keys if key != target_key])


def _remove_pair(value: str) -> None:
    """
    - Removes a pair from the 'KV Pair' CSV if it exists
    - Pairs: <key masked, value>
    """
    target_value = value.lower()

    file_name = ensure_csv_extension(os.path.join(OUTPUT_DIR, KV_PAIRS_FILE_NAME))

    existing_pairs = get_csv_rows(file_name)
    existing_pair_values = [pair[1] for pair in existing_pairs]

    # Re-write w/o target if it exists
    if target_value in existing_pair_values:
        with open(file_name, "w", newline="") as csv_file:
            csv.writer(csv_file).writerow([pair for pair in existing_pairs if pair[1] != target_value])

