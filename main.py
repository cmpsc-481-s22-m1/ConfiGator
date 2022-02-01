"""This file will use all of our functions and run the progam"""
 
import typer

from configator import create_actions_config
from configator import create_gatorgradle_yml
from configator import generate_build_gradle

def main(name: str = typer.Argument("configenerated-assignment")):
    # WARNING: Main method is empty
 
 
if __name__ == '__main__':
    typer.run(main)
    # create_actions_config.create_configator_file()
    # create_gatorgradle_yml.create_gatorgrader()
    # generate_build_gradle.create_gradlebuild()

# TODO: Create functions for validating input and ensuring the user is satisfied with their input

# TODO: Develop default values if the user does not want to input a value, after confirmation of course