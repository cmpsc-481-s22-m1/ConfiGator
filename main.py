"""This file will use all of our functions and run the progam"""
 
import typer

from configator import create_actions_config
from configator import create_gatorgradle_yml
from configator import generate_build_gradle

def main(
    name: str = typer.Argument("configator-generated"),
    brk: str = typer.Argument("true"),
    ff: str = typer.Argument("false"),
    ind: int = typer.Argument(2),
    vers: str = typer.Argument("v1.1.0"),
    vers2: str = typer.Argument("0.5.1"),
    com: int = typer.Argument(3)
):
    typer.echo(f"Generating assignment as: {name}")
    create_gatorgradle_yml.create_gatorgrader(name, brk, ff, ind, vers, com)
 
if __name__ == '__main__':
    typer.run(main)