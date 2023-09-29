import click
from flask.cli import with_appcontext

from .models.db import db


@click.command("create-tables")
@with_appcontext
def create_tables_command():
    """Create new tables."""
    models.db.create_all()
    click.echo("Create all tables.")


@click.command("drop-tables")
@with_appcontext
def drop_tables_command():
    """Clear existing data."""
    models.db.drop_all()
    click.echo("Drop all tables.")
