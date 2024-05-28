import click
from flask.cli import with_appcontext

from .models import db


@click.command("create-tables")
@with_appcontext
def create_tables_command():
    """Create new tables."""
    db.db.create_all()
    click.echo("Create all tables.")


@click.command("drop-tables")
@with_appcontext
def drop_tables_command():
    """Clear existing data."""
    db.db.drop_all()
    click.echo("Drop all tables.")
