import click
from ceas.main import run as run_ceas

@click.group()
def cli():
    pass

@cli.command()
def run():
    """Starts the CEAS application and runs the scheduler."""
    run_ceas()

if __name__ == '__main__':
    cli()
