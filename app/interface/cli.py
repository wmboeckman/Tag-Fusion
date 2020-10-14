from .gui import GUIApp
import click


@click.command()
@click.option('--gui', '--ui', is_flag=True)
def cli(gui):
    if gui:
        GUIApp()
    else:
        pass  # Continue through to rest fo cli app.
