""""Command-line interface to receive input to create configuration files"""

# import necessary libraries
import typer
import os

print("Let's work on getting your configuration files generated!")

cli = typer.Typer()

# directory
directory = "C:/config"

"""
creating directory that can have files 
that can be read and written to
"""

os.mkdir(directory, mode = 0o666)
print("Directory '% s' is built!" % directory)

def cli(
    fastfail: bool = typer.Option(False)
):
    
    """"
    Generating and writing
    to the gatorgrader.yml file
    """

    f = open("C:/config/gatorgrader.yml", "w")
    f.write("""# Should a check failure immediately "break" the Gradle run?\n""")
    f.write(f"fastfail: {fastfail}")
    f.close()

    print("All the necessary configuration files have been created and placed into the '% s'" % directory)

if __name__ == '__main__':
    typer.run(cli)