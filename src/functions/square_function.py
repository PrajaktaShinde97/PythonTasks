# Create a function which will take a positive number from the user and perform square of the number?
# i/o = 3
# o/p = 9


def square_function():
    number= int(input("Enter a number:"))
    if number < 0:
        print("Enter a positive number")
    else:
        square = number*number
        print(f"Square of {number} is {square}")

square_function()