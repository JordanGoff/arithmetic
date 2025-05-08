from random import randint
import os


def clear():
    """Clear the screen."""
    os.system("cls")


def addition(a, b):
    """Execute the addition program."""
    while True:
        # Get the numbers and answer for the problem.
        num1 = randint(a, b)
        num2 = randint(a, b)
        answer = str(num1 + num2)

        # Get the guess from the user.
        guess = input(f"{num1} + {num2} = ")
        clear()

        # Let the user go back.
        if guess == "":
            break

        print(f"{num1} + {num2} = {answer}")

        # Check the guess to the answer.
        if guess == answer:
            print("Correct!")
        else:
            print("Incorrect!")
        
        # Observe the results.
        input()
        clear()


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