from random import randint
import os


def clear():
    """Clear the screen."""
    os.system("cls")


def addition(a, b):
    """Execute the addition program."""
    print("addition")


def subtraction(a, b):
    """Execute the subtraction program."""


def multiplication(a, b):
    """Execute the multiplication program."""

def division(a, b):
    """Execute the division program."""

def main():
    """Execute the program."""
    # Choose a lower bound and upper bound.
    while True:
        try:
            a = int(input("Minimum: "))
            b = int(input("Maximum: "))
            clear()
        except:
            clear()
            break

        # Choose an operation.
        print("(1) Addition")
        print("(2) Subtraction")
        print("(3) Multiplication")
        print("(4) Division\n")
        operation = input("Input: ")
        clear()

        # Run the operation program.
        if operation == "1":
            addition(a, b)
        elif operation == "2":
            subtraction(a, b)
        elif operation == "3":
            multiplication(a, b)
        elif operation == "4":
            division(a, b)
        else:
            continue


main()