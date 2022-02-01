"""This file will use all of our functions and run the progam"""

import typer

from configator import create_actions_config
from configator import create_gatorgradle_yml
from configator import generate_build_gradle

def main(
    name: str = typer.Option("configator-generated"),
    brk: str = typer.Option("true"),
    ff: str = typer.Option("false"),
    ind: int = typer.Option(2),
    vers: str = typer.Option("v1.1.0"),
    ggradleversion: str = typer.Option("0.5.1"),
    com: int = typer.Option(3)
):
    typer.echo(f"Generating assignment as: {name}")
    create_gatorgradle_yml.create_gatorgrader(name, brk, ff, ind, vers, com)
    generate_build_gradle.create_gradlebuild(ggradleversion)

if __name__ == '__main__':
    typer.run(main)
