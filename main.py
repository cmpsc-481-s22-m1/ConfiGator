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
    # Progress bar for visual appeal
    with typer.progressbar(range(100)) as progress:
        for value in progress:
            # Fake processing time
            time.sleep(0.01)
    create_gatorgradle_yml.create_gatorgrader(name, brk, fastfail, ind, vers, com)
    generate_build_gradle.create_gradlebuild(ggradleversion)
    create_actions_config.create_configator_file()
    # Success confirmation message
    typer.secho(f"\nAssignment generation success!", fg = typer.colors.GREEN)

if __name__ == '__main__':
    app()
