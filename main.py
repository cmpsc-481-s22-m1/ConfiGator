"""This file will use all of our functions and run the progam"""
 
import typer

from configator import create_actions_config
from configator import create_gatorgradle_yml
from configator import generate_build_gradle
 
def main(
    # TODO: Reduce parameters here, sort of clunky
    name: str = typer.Argument("new-assignment"),
    brk: bool = typer.Option(True),
    fastfail: bool = typer.Option(False),
    indent: int = typer.Option(4),
    version: str = typer.Option("v1.1.0"),  
    commits: int = typer.Option(3)
):
    # TODO: Present user with a set of defaults on default run to reduce prompting
    """Gather input from the command line to fill config files."""
def main(name: str = typer.Argument("configenerated-assignment")):
    # WARNING: Main method is empty
 
 
if __name__ == '__main__':
    typer.run(main)
    # create_actions_config.create_configator_file()
    # create_gatorgradle_yml.create_gatorgrader()
    # generate_build_gradle.create_gradlebuild()

# TODO: Create functions for validating input and ensuring the user is satisfied with their input

# TODO: Develop default values if the user does not want to input a value, after confirmation of course