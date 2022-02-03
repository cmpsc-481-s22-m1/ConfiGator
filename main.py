"""The file will use all of our functions and run the progam"""

import typer

from configator import create_actions_config
from configator import create_gatorgradle_yml
from configator import generate_build_gradle
from decouple import config as dc

# Set defaults equal to values in .env file
NAME = dc('NAME')
BRK = dc('BRK')
FASTFAIL = dc('FASTFAIL')
INDENT = dc('INDENT')
VERSION = dc('VERSION')
GGRADLEVERSION = dc('GGRADLEVERSION')
COMMITS = dc('COMMITS')

@app.command()
def config():
    # Menu stating current default configurations
    typer.echo(f"Default Configurations")
    typer.echo(f"1. Generated directory name: " + NAME)
    typer.echo(f"2. Run stops on first error: " + BRK)
    typer.echo(f"3. Fail upon first failed check: " + FASTFAIL)
    typer.echo(f"4. Indent: " + INDENT)
    typer.echo(f"5. Version " + VERSION)
    typer.echo(f"6. GatorGradle Version: " + GGRADLEVERSION)
    typer.echo(f"7. Commits: " + COMMITS)
    # Prompt the user for the value they want to modify
    option = typer.prompt(f"Enter the number of the configuration you would like to change: ")
    selection = None
    # Use if/elif logic because switch cases do not natively exist in Python
    if option == 1:
        selection = "generated file name"
        NAME = typer.prompt(f"Enter desired default directory name: ")
    elif option == 2:
        selection = "runs stops on first error"
        BRK = typer.prompt(f"Enable (True) or disable (False) the run stopping upon first error: ")
    elif option == 3:
        selection = "fail upon first failed check"
        FASTFAIL = typer.prompt(f"Enable (True) or disable (False) fails upon first failed check: ")
    elif option == 4:
        selection = "indent"
        INDENT = typer.prompt(f"Set desired indent: ")
    elif option == 5:
        selection = "version"
        VERSION = typer.prompt(f"Enter desired version (vX.X.X): ")
    elif option == 6:
        selection = "GatorGradle version"
        GGRADLEVERSION = typer.prompt(f"Enter desired GatorGradle version (X.X.X): ")
    elif option == 7:
        selection == "commits minimum"
        COMMITS = typer.prompt(f"Enter default minimum commits value: ")
    # Run rewrite_env() function to rewrite the .env file with desired values
    rewrite_env(NAME, BRK, FASTFAIL, INDENT, VERSION, GGRADLEVERSION, COMMITS)
    # Print completion message to console upon value overwrite
    typer.echo(f"You have successly changed the " + selection + " configuration...")

def rewrite_env(
    NAME,
    BRK,
    FASTFAIL,
    INDENT,
    VERSION,
    GGRADLEVERSION,
    COMMITS
):
    # Open the .env file for modifications
    e = open(f"../.env", "w")
    # Write each value to the .env file
    e.write(f"NAME=" + NAME + "\n")
    e.write(f"BRK=" + BRK + "\n")
    e.write(f"FASTFAIL=" + FASTFAIL + "\n")
    e.write(f"INDENT=" + INDENT + "\n")
    e.write(f"VERSION=" + VERSION + "\n")
    e.write(f"GGRADLEVERSION=" + GGRADLEVERSION + "\n")
    e.write(f"COMMITS=" + COMMITS)
    # Close .env file
    e.close()

def main(arg: Optional[str] = typer.argument(None)):
    typer.echo(f"Generating assignment as: {name}")
    create_gatorgradle_yml.create_gatorgrader(name, brk, fastfail, ind, vers, com)
    generate_build_gradle.create_gradlebuild(ggradleversion)

if __name__ == '__main__':
    typer.run(main)
