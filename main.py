"""The file will use all of our functions and run the progam"""

import time
import typer

from configator import create_actions_config
from configator import create_gatorgradle_yml
from configator import generate_build_gradle
from decouple import config as dc
from typing import Optional

# TODO: Check to see if needed packages are installed in pyproject.toml
# TODO: Have team member test program because of Python version drama
# TODO: Update String syntax for echo calls from "..." + var + "..." to "... {var}"
# TODO: Cry over program testing drama

app = typer.Typer()

# Set defaults equal to values in .env file
name = dc('NAME')
brk = dc('BRK')
fastfail = dc('FASTFAIL')
indent = dc('INDENT')
version = dc('VERSION')
ggradleversion = dc('GGRADLEVERSION')
commits = dc('COMMITS')

@app.command()
def config():
    """List default configurations and give the user the opportunity to modify defaults"""
    # Menu stating current default configurations
    typer.echo(f"Default Configurations")
    global name, brk, fastfail, indent, version, ggradleversion, commits
    typer.echo(f"1. Generated directory name: " + name)
    typer.echo(f"2. Run stops on first error: " + brk)
    typer.echo(f"3. Fail upon first failed check: " + fastfail)
    typer.echo(f"4. Indent: " + indent)
    typer.echo(f"5. Version " + version)
    typer.echo(f"6. GatorGradle Version: " + ggradleversion)
    typer.echo(f"7. Commits: " + commits)
    # Prompt the user for the value they want to modify
    option = typer.prompt(f"Enter the number of the configuration you would like to change: ")
    selection = ""
    # Use if/elif logic because switch cases do not natively exist in Python
    if option == 1:
        selection = "generated file name"
        name = typer.prompt(f"Enter desired default directory name: ")
    elif option == 2:
        selection = "runs stops on first error"
        brk = typer.prompt(f"Enable (True) or disable (False) the run stopping upon first error: ")
    elif option == 3:
        selection = "fail upon first failed check"
        fastfail = typer.prompt(f"Enable (True) or disable (False) fails upon first failed check: ")
    elif option == 4:
        selection = "indent"
        indent = typer.prompt(f"Set desired indent: ")
    elif option == 5:
        selection = "version"
        version = typer.prompt(f"Enter desired version (vX.X.X): ")
    elif option == 6:
        selection = "GatorGradle version"
        ggradleversion = typer.prompt(f"Enter desired GatorGradle version (X.X.X): ")
    elif option == 7:
        selection == "commits minimum"
        commits = typer.prompt(f"Enter default minimum commits value: ")
    # Run rewrite_env() function to rewrite the .env file with desired values
    rewrite_env(name, brk, fastfail, indent, version, ggradleversion, commits)
    # Print completion message to console upon value overwrite
    typer.echo(f"You have successly changed the " + selection + " configuration...")

@app.command()
def rewrite_env(
    name,
    brk,
    fastfail,
    indent,
    version,
    ggradleversion,
    commits
):
    """Modify defaults within the .env file"""
    # Open the .env file for content modification
    e = open(f"../.env", "w")
    # Write each value to the .env file
    e.write(f"NAME=" + name + "\n")
    e.write(f"BRK=" + brk + "\n")
    e.write(f"FASTFAIL=" + fastfail + "\n")
    e.write(f"INDENT=" + indent + "\n")
    e.write(f"VERSION=" + version + "\n")
    e.write(f"GGRADLEVERSION=" + ggradleversion + "\n")
    e.write(f"COMMITS=" + commits)
    # Close .env file
    e.close()

def main(arg: Optional[str] = typer.Argument(None)):
    if arg is None:
        # Added simulated progress bar
        with typer.progressbar(range(100)) as progress:
            for value in progress:
                time.sleep(0.01)
        # Modify files as intended
        create_gatorgradle_yml.create_gatorgrader(name, brk, fastfail, indent, version, commits)
        generate_build_gradle.create_gradlebuild(ggradleversion)
    else:
        # Run config to enable changing defaults via .env file
        config_run = True
        config()
        # Add input validation for config()
        while config_run:
            # Prompt user for continuation of configuring defaults
            answer = typer.prompt("Would you like to continue configuring defaults? (Y/N): ")
            # if-else logic for user answer to ensure input validation
            if answer == 'Y' or answer == 'N':
                # Case where answer is yes (Y) and config runs again
                if answer == 'Y':
                    config()
                # Case where answer is no (N) and breaks while loop with config_run now equaling False
                elif answer == 'N':
                    config_run = False
            # Case where user inputs invalid answer
            else:
                answer = typer.echo("\nInvalid input...")
        # User message for run changes
        typer.echo(f"Run the program again to see your changes...")

if __name__ == '__main__':
    typer.run(main)
