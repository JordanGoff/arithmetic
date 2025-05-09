# Practice for addition, subtraction, multiplication, and division.

from random import randint
import os


def clear():
    """Clear the screen."""
    os.system("cls")


def compute(a, b, operation):
    """Run the main program."""
    while True:
        # Get the numbers for the problem.
        num1 = randint(a, b)
        num2 = randint(a, b)

        # Get the answer for the problem.
        if operation == "1":
            (answer, opp) = addition(num1, num2)
        elif operation == "2":
            (answer, opp) = subtraction(num1, num2)
        elif operation == "3":
            (answer, opp) = multiplication(num1, num2)
        elif operation == "4":
            (answer, opp) = division(num1, num2)
        else:
            return None
        
        # Write the question.
        question = f"{num1} {opp} {num2} = "
        
        # Get the guess from the user.
        guess = input(question)
        clear()

        # Check if the user wants to go back.
        if guess == "":
            return None
        
        # Show the answer.
        print(f"{question}{answer}")

        # Check if the guess is correct.
        if guess == answer:
            print("\033[32mCorrect!\033[0m")
        else:
            print("\033[31mIncorrect!\033[0m")
        
        # Observe the correct answer.
        input()
        clear()


def addition(num1, num2):
    """Execute the addition program."""
    answer = str(num1 + num2)
    return (answer, "+")


def subtraction(num1, num2):
    """Execute the subtraction program."""
    answer = str(num1 - num2)
    return (answer, "-")


def multiplication(num1, num2):
    """Execute the multiplication program."""
    answer = str(num1 * num2)
    return (answer, "*")


def division(num1, num2):
    """Execute the division program."""
    answer = str(num1 // num2) + " r " + str(num1 % num2)
    return (answer, "/")


def main():
    """Execute the program."""
    clear()

    # Choose a lower bound and upper bound.
    while True:
        try:
            a = int(input("Minimum: "))
            b = int(input("Maximum: "))
            clear()
        except:
            clear()
            break

        # Initialize the loop.
        operation = " "

        while operation != "":
            # Choose an operation.
            print("(1) Addition")
            print("(2) Subtraction")
            print("(3) Multiplication")
            print("(4) Division\n")
            operation = input("Input: ")
            clear()

            # Run the main program.
            compute(a, b, operation)


main()