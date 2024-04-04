from src.utils.csv_utils import delete_csv, delete_csv_row, ensure_csv_extension, get_csv_rows, append_csv_row
from src.constants.consts import API_KEYS_FILE_NAME, KV_PAIRS_FILE_NAME, OUTPUT_DIR
from src.utils.string_utils import mask_string, generate_key
from src.utils.decorators import ensure_files_exist
import click
import os


# INVARIANTS:
#   - All seed values are converted to lowercase


FQ_API_KEYS_FILE_NAME = ensure_csv_extension(os.path.join(OUTPUT_DIR, API_KEYS_FILE_NAME))
FQ_KV_PAIRS_FILE_NAME = ensure_csv_extension(os.path.join(OUTPUT_DIR, KV_PAIRS_FILE_NAME))


@click.group()
def cli():
    pass


@cli.command("list")
@ensure_files_exist
def list() -> None:
    """Lists all pairs of keys and corresponding values"""
    rows = get_csv_rows(FQ_KV_PAIRS_FILE_NAME)

    if len(rows) == 0:
        click.echo("Nothing to show...")

    for idx, row in enumerate(rows):
        max_width = max(len(row[0]), len(row[1]))
        click.echo(f"{idx}: {row[1].ljust(max_width)} has key\t{row[0]}")


@cli.command("add")
@click.option("-v", "--value", type=str, prompt="Seed value")
@ensure_files_exist
def add(value: str) -> None:
    """
    - Generates a new key based on the value
    - Adds the new key to 'Keys' CSV
    - Adds a relationship record between the Value and Key in 'KV Pairs' CSV
    - Throws if value already exists
    """
    # Gen and format new values
    new_value = value.lower()
    key = generate_key(new_value)
    existing_pair_values = [row[1] for row in get_csv_rows(FQ_KV_PAIRS_FILE_NAME)]

    # Guard: confirm value not taken
    if new_value in existing_pair_values:
        raise ValueError(f"Key already exists for '{new_value}'")

    append_csv_row(FQ_API_KEYS_FILE_NAME, key)
    append_csv_row(FQ_KV_PAIRS_FILE_NAME, [mask_string(key), new_value])

    click.echo(f"Added new key for {new_value}: {key}")


@cli.command("revoke")
@click.option("-v", "--value", type=str, prompt="Seed value")
@ensure_files_exist
def revoke(value: str) -> None:
    """Revokes an existing key"""

    confirmation = click.prompt(f"Are you sure you want to delete {value}'s key ? (y/n)")

    if confirmation.lower().strip() != "y":
        click.echo("Aborting")
        return

    # Gen and format new values
    target_value = value.lower()
    target_key = generate_key(target_value)

    delete_csv_row(FQ_API_KEYS_FILE_NAME, target_key)
    delete_csv_row(FQ_KV_PAIRS_FILE_NAME, target_value)

    click.echo(f"Key revoked for {target_value}")


@cli.command("nuke")
@ensure_files_exist
def nuke() -> None:
    """Nukes all CSV files"""

    confirmation = click.prompt(f"Are you sure you want to delete all CSV files in {OUTPUT_DIR} dir ? (y/n)")

    if confirmation.lower().strip() != "y":
        click.echo("Aborting")
        return

    delete_csv(OUTPUT_DIR)

    click.echo("CSVs deleted")
