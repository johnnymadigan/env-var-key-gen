from src.utils.csv_utils import delete_csv, get_csv_rows, add_key, remove_key_for_value
from src.utils.decorators import ensure_files_exist, handle_errors
from src.constants.consts import KV_PAIRS_FILE_NAME, OUTPUT_DIR
import click
import os


@click.group()
def cli():
    pass


@cli.command("list")
@ensure_files_exist
@handle_errors
def list() -> None:
    """Lists all pairs of keys and corresponding values"""
    fq_csv_name = os.path.join(OUTPUT_DIR, KV_PAIRS_FILE_NAME)
    rows = get_csv_rows(fq_csv_name)

    if len(rows) == 0:
        click.echo("Nothing to show...")

    for idx, row in enumerate(rows):
        max_width = max(len(row[0]), len(row[1]))
        click.echo(f"{idx}: {row[1].ljust(max_width)} has key\t{row[0]}")


@cli.command("add")
@click.option("-v", "--value", type=str, prompt="Seed value")
@ensure_files_exist
@handle_errors
def add(value: str) -> None:
    """Creates and saves a new key given a seed value"""

    key = add_key(value)

    click.echo(f"Added new key for {value}: {key}")


@cli.command("revoke")
@click.option("-v", "--value", type=str, prompt="Seed value")
@ensure_files_exist
@handle_errors
def revoke(value: str) -> None:
    """Revokes an existing key"""

    confirmation = click.prompt(f"Are you sure you want to delete {value}'s key ? (y/n)")

    if confirmation.lower().strip() != "y":
        click.echo("Aborting")
        return

    remove_key_for_value(value)

    click.echo(f"Key removed for {value}")

@cli.command("nuke")
@ensure_files_exist
@handle_errors
def nuke() -> None:
    """Nukes all CSV files"""

    confirmation = click.prompt(f"Are you sure you want to delete all CSV files in {OUTPUT_DIR} dir ? (y/n)")

    if confirmation.lower().strip() != "y":
        click.echo("Aborting")
        return

    delete_csv()

    click.echo("CSVs deleted")