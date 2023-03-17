import typer

app = typer.Typer()

@app.command()
def python-cli-typer(string: str = typer.Argument(..., help = )):
print("@scott")
print(string)

app()