""""Command-line interface to receive input to create configuration files"""

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
    indentation: bool = typer.Option(False)
):

    print(f"Indentation: {indentation}")
    
    """"Generating the gatorgrader.yml file"""

    f = open("C:/config/gatorgrader.yml", "w")
    f.write("""# Implementing indentation for Gradle run\n""")
    f.write("indentation: 2")
    f.close()

    print("All the necessary configuration files have been created and placed into the '% s'" % directory)

if __name__ == '__main__':
    cli()