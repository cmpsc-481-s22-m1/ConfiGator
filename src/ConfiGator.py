""""Command-line interface to receive input to create configuration files"""

import typer

def cli(
    fastfail: bool = typer.Option(False)
):
    print(f"Fastfail: {fastfail}")
    
    """"Generating the gatorgrader.yml file"""

    f = open("gatorgrader.yml", "w")
    f.write("fastfail: false")
    f.close()

if __name__ == '__main__':
    cli()