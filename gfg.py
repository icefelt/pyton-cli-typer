# Python program to print
# square or cube of a number
import typer

app = typer.Typer()

@app.command()
def square(number: int):
	print(number*number)

@app.command()
def cube(number: int):
	print(number*number*number)

app()
