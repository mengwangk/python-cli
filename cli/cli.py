#!/usr/bin/env python
"""
A sample python cli.
"""

import click


@click.group()
def cli():
    """Cli."""


@click.command()
@click.argument('src_db')
@click.argument('dest_db')
def command1(src_db, dest_db):
    """Command 1."""
    click.echo('command 1 ')
    click.echo(src_db)
    click.echo(dest_db)


@click.command()
@click.argument('src_db')
@click.argument('dest_db')
def command2(src_db, dest_db):
    """Command 2."""
    click.echo('command 2')
    click.echo(src_db)
    click.echo(dest_db)


cli.add_command(command1)
cli.add_command(command2)

if __name__ == '__main__':
    cli()
