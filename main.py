"""This file will use all of our functions and run the progam"""
 
import typer
from configator import create_actions_config
from configator import create_gatorgradle_yml
from configator import generate_build_gradle
 
def main(
    name: str = typer.Option("New Assignment"),
    brk: bool = typer.Option(False),
    fastfail: bool = typer.Option(False),
    indent: int = typer.Option(4),
    version: str = typer.Option("v1.1.0"),  
    commits: int = typer.Option(3)
):
    """Gather input from the command line to fill config files."""
    typer.echo("")
    typer.echo(f"The name of your assignment is: {name}")
    typer.echo("")
    typer.echo(f"Will your assignment break the Gradle run when a check fails: {brk}")
    typer.echo("")
    typer.echo(f"Will your assignment immediately break the Gradle run at the first check fail: {fastfail}")
    typer.echo("")
    typer.echo(f"This file will use level {indent} indentation")
    typer.echo("")
    typer.echo(f"Your assignment uses version {version} of GatorGradle")
    typer.echo("")
    typer.echo(f"Your assignment will require {commits} commits.")
    typer.echo("")
 
 
if __name__ == '__main__':
    typer.run(main)
    # create_actions_config.create_configator_file()
    # create_gatorgradle_yml.create_gatorgrader()
    # generate_build_gradle.create_gradlebuild()