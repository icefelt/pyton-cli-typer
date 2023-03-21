import typer

app = typer.Typer()

@app.command()
def gfg(string: str = typer.Argument(..., help = """Prints input string""")):
	"""Prints geeksforgeeks and input string"""
	print("@geeksforgeeks")
	print(string)

app()
