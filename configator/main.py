"""This file will use all of our functions and run the program"""

import typer

# Import from configator
from configator import create_actions_config
from configator import create_gatorgradle_yml
from configator import generate_build_gradle

#pylint: disable=too-many-arguments
app = typer.Typer()
@app.command()
def main(

    name: str = typer.Option("configator-generated"),
    brk: str = typer.Option("true"),
    fastfail: str = typer.Option("false"),
    indent: int = typer.Option(2),
    version: str = typer.Option("master"),
    ggradleversion: str = typer.Option("0.5.1"),
):

    """This function will run functions to generate files"""

    # Alert user of assignment generation under specified name
    typer.echo(f"\nGenerating assignment as: {name}\n")

    # Progress bar to measure progress of necessary program functions
    try:
        with typer.progressbar(length=99) as progress:
            create_gatorgradle_yml.create_gatorgrader(name, brk, fastfail, indent, version)
            progress.update(33)
            generate_build_gradle.create_gradlebuild(ggradleversion)
            progress.update(33)
            create_actions_config.create_configator_file()
            progress.update(33)
        # Success confirmation message
        typer.secho("\nAssignment generation success!", fg = typer.colors.GREEN)
    except: # pylint: disable=bare-except
        typer.secho("\nAn error occurred in assignment generation...", fg = typer.colors.RED,
        err = True)

if __name__ == '__main__':
    app()
