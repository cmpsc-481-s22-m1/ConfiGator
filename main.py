"""This file will use all of our functions and run the progam"""
 
import typer

from configator import create_actions_config
from configator import create_gatorgradle_yml
from configator import generate_build_gradle

"""Global variables assigned as configuration defaults"""
brk = False
ff = False
ind = 4
vers = "v1.1.0"
com = 3

# NOTE: The current implementation serves as purpose for structure, upon collaboration up to change

@app.command()
def create(name: str = typer.Argument("configator-generated")):
    typer.echo(f"Generating assignment as: {name}")

@app.command()
def config():
    # Print out current configuration settings
    # NOTE: Potentially consider pulling values from env file, but honestly idk if that's valid in Python
    typer.echo(f"Configuration Settings")
    # TODO: Stylistic concern, add divider to break heading from body
    typer.echo(f"Program breaks when check fails: {get_brk()}")
    typer.echo(f"Assignment fails at first check fail: {get_ff()}")
    typer.echo(f"Indentation level: {get_indent()}")
    typer.echo(f"GatorGradle version: {get_version()}")
    typer.echo(f"Minimum required commits: {get_commits()}")
    # TODO: Give configuraion customization

# TODO: For each of the accessor and mutator methods, investiage functions to refactor for simpilicity

def set_brk(brk_input):
    brk = brk_input

def get_brk():
    return brk

def set_ff(fast_fail):
    ff = fast_fail

def get_ff():
    return ff

def set_indent(indent):
    ind = indent

def get_indent():
    return ind

def set_version(version):
    vers = version

def get_version():
    return vers

# TODO: Investigate the purpose of the "commits" variable and how it is intended to be used
def set_commits(commits):
    com = commits

def get_commits():
    return com

# TODO: Complete main method
def main():
 
 
if __name__ == '__main__':
    typer.run(main)
    # create_actions_config.create_configator_file()
    # create_gatorgradle_yml.create_gatorgrader()
    # generate_build_gradle.create_gradlebuild()

# TODO: Create functions for validating input and ensuring the user is satisfied with their input

# TODO: Develop default values if the user does not want to input a value, after confirmation of course