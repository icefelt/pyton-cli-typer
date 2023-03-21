import typer

app = typer.Typer()

@app.command()
# You can input a default value like
# 'True' or 'False' instead of '...'
# in typer.Option() below.
def square(name,language: bool = typer.Option(
..., prompt = "Do You Want to print the language"),
		display: bool = False):
	print("Scotty Wins!")
	
	if display == True:
		print(name)
	if language == True:
		print("Python 3.6+")

app()
