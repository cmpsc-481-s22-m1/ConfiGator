""""Command-line interface to receive input to create configuration files"""

import typer

def cli(
    indentation: bool = typer.Option(False)
):

    print(f"Indentation: {indentation}")
    
    """"Generating the gatorgrader.yml file"""

    f = open("gatorgrader.yml", "w")
    f.write("indentation: 2")
    f.close()

if __name__ == '__main__':
    cli()