from src.utils.csv_utils import add_key, get_csv_rows, remove_key, remove_pair
from src.constants.consts import KV_PAIRS_FILE_NAME
from src.utils.key_utils import generate_key
import click

# INVARIANTS:
#   - All seed values are converted to lowercase


@click.group()
def cli():
    pass


@cli.command("list")
def list() -> None:
    """Lists all pairs of keys and corresponding values"""
    rows = get_csv_rows(KV_PAIRS_FILE_NAME)

    if len(rows) == 0:
        click.echo("Nothing to show...")

    for idx, row in enumerate(rows):
        max_width = max(len(row[0]), len(row[1]))
        click.echo(f"{idx}: {row[1].ljust(max_width)} has key\t{row[0]}")


@cli.command("add")
@click.option("-v", "--value", type=str, prompt="Seed value")
def add(value: str) -> None:
    """Creates and saves a new key given a seed value"""

    value_formatted = value.lower()
    key = generate_key(value_formatted)

    add_key(value_formatted, key)

    click.echo(f"Added new key for {value}: {key}")


@cli.command("revoke")
@click.option("-v", "--value", type=str, prompt="Seed value")
def revoke(value: str) -> None:
    """Revokes an existing key"""

    user_input = input(f"Are you sure you want to delete {value}'s key ? (y/n) ")

    if user_input.lower().strip() != "y":
        click.echo("Aborting")
        return

    value_formatted = value.lower()
    key = generate_key(value_formatted)

    remove_key(key)
    remove_pair(value_formatted)

    click.echo(f"Key removed for {value}")
