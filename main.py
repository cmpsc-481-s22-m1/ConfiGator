"""This file will use all of our functions and run the program"""

import time
import typer

# Import from configator
from configator import create_actions_config
from configator import create_gatorgradle_yml
from configator import generate_build_gradle

app = typer.Typer()
@app.command()
def main(
    name: str = typer.Option("configator-generated"),
    brk: str = typer.Option("true"),
    fastfail: str = typer.Option("false"),
    ind: int = typer.Option(2),
    vers: str = typer.Option("v1.1.0"),
    ggradleversion: str = typer.Option("0.5.1"),
    com: int = typer.Option(3)
):
    # Alert user of assignment generation under specified name
    typer.echo(f"\nGenerating assignment as: {name}\n")
    # Progress bar to measure progress of necessary program functions
    total = 99
    try:
        with typer.progressbar(length=total) as progress:
            create_gatorgradle_yml.create_gatorgrader(name, brk, fastfail, ind, vers, com)
            progress.update(33)
            generate_build_gradle.create_gradlebuild(ggradleversion)
            progress.update(33)
            create_actions_config.create_configator_file()
            progress.update(33)
        # Success confirmation message
        typer.secho(f"\nAssignment generation success!", fg = typer.colors.GREEN)
    except:
        typer.secho(f"\nAn error occurred in assignment generation...", fg = typer.colors.RED)


if __name__ == '__main__':
    app()
