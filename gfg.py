# Python program to print "Hello World!"
# By taking passing argument value as "World!" in parameter name
import typer


# Function having parameter name
def main(name):
	print(f"Hello {name}")

typer.run(main)
