"""This file will use all of our functions and run the progam"""
 
import typer

from configator import create_actions_config
from configator import create_gatorgradle_yml
from configator import generate_build_gradle
 
def main(
    name: str = typer.Argument("new-assignment"),
    brk: bool = typer.Option(True),
    fastfail: bool = typer.Option(False),
    indent: int = typer.Option(4),
    version: str = typer.Option("v1.1.0"),  
    commits: int = typer.Option(3)
):
    # TODO: Present user with a set of defaults on default run to reduce prompting
    """Gather input from the command line to fill config files."""
    typer.echo("")
    #name = typer.prompt("What do you want to name your assignment?")
    typer.echo(f"The name of your assignment is: {name}")
    typer.echo("")
    #brk = typer.prompt("Will the Gradle run break when a check fails?")
    typer.echo(f"Will your assignment break the Gradle run when a check fails: {brk}")
    typer.echo("")
    #fastfail = typer.prompt("Will your assignment fail at the first check fail?")
    typer.echo(f"Will your assignment immediately break the Gradle run at the first check fail: {fastfail}")
    typer.echo("")
    #indent = typer.prompt("What level of indentation will your assignment require?")
    typer.echo(f"This file will use level {indent} indentation")
    typer.echo("")
    #version = typer.prompt("What version of GatorGradle will be used for this assignment?")
    typer.echo(f"Your assignment uses version {version} of GatorGradle")
    typer.echo("")
    #commits = typer.prompt("How many commits will your assignment require?")
    typer.echo(f"Your assignment will require {commits} commits.")
    typer.echo("")
 
 
if __name__ == '__main__':
    typer.run(main)
    # create_actions_config.create_configator_file()
    # create_gatorgradle_yml.create_gatorgrader()
    # generate_build_gradle.create_gradlebuild()

# TODO: Create functions for validating input and ensuring the user is satisfied with their input

# TODO: Develop default values if the user does not want to input a value, after confirmation of course