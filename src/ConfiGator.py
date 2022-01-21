import typer

def cli(
    fastfail: bool = typer.Option(False)
):

print(f"Fastfail: {fastfail}")

if __name__ == '__main__':
    typer.run(cli)