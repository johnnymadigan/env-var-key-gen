from src.utils.string_utils import remove
import fnmatch
import csv
import os


def ensure_csv_extension(file_name: str) -> str:
    return file_name if file_name.endswith(".csv") else file_name + ".csv"


def throw_if_csv_not_found(file_name: str):
    csv_name = ensure_csv_extension(file_name)

    if not os.path.exists(csv_name):
        raise FileNotFoundError(f"File '{csv_name}' not found")


def get_csv_rows(file_name: str) -> list[list[str]]:
    csv_name = ensure_csv_extension(file_name)

    throw_if_csv_not_found(csv_name)

    with open(csv_name, newline="") as csv_file:
        res = [row for row in csv.reader(csv_file)]
        return res


def delete_csv(dir_path: str) -> None:
    for file in os.listdir(dir_path):
        if fnmatch.fnmatch(file, "*.csv"):
            csv_file = os.path.join(dir_path, file)
            os.remove(csv_file)


def append_csv_row(file_name: str, row: str | list[str]) -> None:
    csv_name = ensure_csv_extension(file_name)

    throw_if_csv_not_found(csv_name)

    with open(csv_name, "a", newline="") as csv_file:
        if isinstance(row, list):
            csv.writer(csv_file).writerow(row)
        else:
            csv.writer(csv_file).writerow([row])


def delete_csv_row(file_name: str, target: str) -> None:
    """
    - Deletes a single CSV row if contains the target value (case-insensitive)
    - Throws if file does not exist
    - Throws if value already deleted from CSV
    """
    csv_name = ensure_csv_extension(file_name)

    throw_if_csv_not_found(csv_name)

    existing_rows = get_csv_rows(file_name)
    updated_rows = remove(existing_rows, target)

    if len(existing_rows) == len(updated_rows):
        raise ValueError(f"'{target}' already deleted")
    
    with open(file_name, "w", newline="") as csv_file:
        if all(isinstance(row, list) for row in updated_rows):
            csv.writer(csv_file).writerows(updated_rows)
        else:
            csv.writer(csv_file).writerows([[row] for row in updated_rows])
