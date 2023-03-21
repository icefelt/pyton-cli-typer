# Python program to take multiple
# inputs of different datatypes and print it
import typer

# Function with multiple parameters
def details(display: bool, name: str, age: int,
			marks: float, country: str = "United States"):
	
	print(f"Country: {country}")
	if display == True:
		print("@geeksforgeeks")
	print(f"Name: {name}")
	print(f"Age: {age}")
	print(f"Marks: {marks}")


typer.run(details)
