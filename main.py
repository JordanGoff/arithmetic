# Practice for addition, subtraction, multiplication, and division.

from random import randint
from math import *
import os


def clear():
    """Clear the screen."""
    os.system("cls")


def rounded(x):
    """Round x to the nearest tenth."""
    return round(10 * x) / 10


def addition(a, b, constant=False):
    """Run the addition program."""
    while True:
        # Get the answer and obtain the guess from the user.
        num1 = randint(a, b)
        num2 = randint(a, b)
        question = f"{num1} + {num2} = "
        answer = num1 + num2
        guess = input(question)
        clear()

        # Check if the user wants to go back.
        if guess == "":
            break

        # Check if the guess is a string.
        try:
            guess = float(guess)
        except:
            print(f"{question}{answer}")
            print("\033[31mIncorrect!\033[0m")
            input()
            clear()
            continue

        # Print the answer.
        print(f"{question}{answer}")

        # Display if the user is correct or incorrect.
        if guess == answer:
            print("\033[32mCorrect!\033[0m")
        else:
            print("\033[31mIncorrect!\033[0m")
        
        # Wait for user input.
        input()
        clear()


def subtraction(a, b, constant=False):
    """Run the subtraction program."""
    while True:
        # Get the answer and obtain the guess from the user.
        num1 = randint(a, b)
        num2 = randint(a, b)
        question = f"{num1} - {num2} = "
        answer = num1 - num2
        guess = input(question)
        clear()

        # Check if the user wants to go back.
        if guess == "":
            break

        # Check if the guess is a string.
        try:
            guess = float(guess)
        except:
            print(f"{question}{answer}")
            print("\033[31mIncorrect!\033[0m")
            input()
            clear()
            continue

        # Print the answer.
        print(f"{question}{answer}")

        # Display if the user is correct or incorrect.
        if guess == answer:
            print("\033[32mCorrect!\033[0m")
        else:
            print("\033[31mIncorrect!\033[0m")
        
        # Wait for user input.
        input()
        clear()


def multiplication(a, b, constant=False):
    """Run the multiplication program."""
    while True:
        # Get the answer and obtain the guess from the user.
        num1 = randint(a, b)
        num2 = randint(a, b)
        question = f"{num1} * {num2} = "
        answer = num1 * num2
        guess = input(question)
        clear()

        # Check if the user wants to go back.
        if guess == "":
            break

        # Check if the guess is a string.
        try:
            guess = float(guess)
        except:
            print(f"{question}{answer}")
            print("\033[31mIncorrect!\033[0m")
            input()
            clear()
            continue

        # Print the answer.
        print(f"{question}{answer}")

        # Display if the user is correct or incorrect.
        if guess == answer:
            print("\033[32mCorrect!\033[0m")
        else:
            print("\033[31mIncorrect!\033[0m")
        
        # Wait for user input.
        input()
        clear()


def division(a, b, constant=False):
    """Run the division program."""
    while True:
        # Obtain the guess from the user.
        num1 = randint(a, b)
        num2 = randint(a, b)
        question = f"{num1} / {num2} = "
        guess = input(question)
        clear()

        # Check if the user wants to go back.
        if guess == "":
            break

        # Perform the appropriate division problem.
        # Indeterminate.
        if num1 == 0 and num2 == 0:
            answer = "Indeterminate"
            print(f"{question}{answer}")
            if guess.lower() == answer.lower():
                print("\033[32mCorrect!\033[0m")
            else:
                print("\033[31mIncorrect!\033[0m")
        # Undefined.
        elif num2 == 0:
            answer = "Undefined"
            print(f"{question}{answer}")
            if guess.lower() == answer.lower():
                print("\033[32mCorrect!\033[0m")
            else:
                print("\033[31mIncorrect!\033[0m")
        # Not indeterminate or undefined.
        else:
            # Decimal.
            try:
                answer = rounded(num1 / num2)
                guess = rounded(float(guess))
                print(f"{question}{answer}")
                if guess == answer:
                    print("\033[32mCorrect!\033[0m")
                else:
                    print("\033[31mIncorrect!\033[0m")
            # Quotient and remainder.
            except:
                answer = str(num1 // num2) + " r " + str(num1 % num2)
                print(f"{question}{answer}")
                if guess.replace(" ", "") == answer.replace(" ", ""):
                    print("\033[32mCorrect!\033[0m")
                else:
                    print("\033[31mIncorrect!\033[0m")

        # Wait for user input.
        input()
        clear()


def square(a, b):
    """Run the square program."""
    while True:
        # Get the answer and obtain the guess from the user.
        num = randint(a, b)
        question = f"{num}² = "
        answer = num ** 2
        guess = input(question)
        clear()

        # Check if the user wants to go back.
        if guess == "":
            break

        # Check if the guess is a string.
        try:
            guess = float(guess)
        except:
            print(f"{question}{answer}")
            print("\033[31mIncorrect!\033[0m")
            input()
            clear()
            continue

        # Print the answer.
        print(f"{question}{answer}")

        # Display if the user is correct or incorrect.
        if guess == answer:
            print("\033[32mCorrect!\033[0m")
        else:
            print("\033[31mIncorrect!\033[0m")
        
        # Wait for user input.
        input()
        clear()


def calculator():
    """Run the calculator program."""
    while True:
        flag = False
        clear()

        # Obtain the expression from the user.
        expression = input()
        clear()

        # Check if the user wants to go back.
        if expression == "":
            break

        # Allow exponential calculations.
        if "^" in expression:
            expression_modified = expression.replace("^", "**")
            flag = True
        
        # Allow factorial calculations.
        if "!" in expression:
            try:
                expression_modified = expression.replace("!", "")
                expression_modified = str(factorial(int(expression_modified)))
                flag = True
            except:
                continue

        # Calculate the expression.
        try:
            if flag:
                answer = eval(expression_modified)
            else:
                answer = eval(expression)
            print(f"{expression} = \033[32m{answer}\033[0m")
            input()
        except:
            continue


def main():
    """Execute the program."""
    clear()

    while True:
        # Choose the minimum number.
        while True:
            a = input("Minimum: ")
            clear()
            if a == "":
                return None
            try:
                a = int(a)
                break
            except:
                continue
        
        # Choose the maximum number.
        while True:
            print(f"Minimum: {a}")
            b = input("Maximum: ")
            clear()
            if b == "":
                break
            try:
                b = int(b)
                break
            except:
                continue
        
        # Go back to the minimum number.
        if b == "" or a > b:
            continue

        # Initialize the loop.
        operator = " "

        while operator != "":
            # Choose an operator.
            print("(1) Addition")
            print("(2) Subtraction")
            print("(3) Multiplication")
            print("(4) Division")
            print("(5) Square")
            print("(6) Calculator\n")
            operator = input("Input: ")
            clear()

            # Run the operator program.
            if operator == "1":
                addition(a, b)
            elif operator == "2":
                subtraction(a, b)
            elif operator == "3":
                multiplication(a, b)
            elif operator == "4":
                division(a, b)
            elif operator == "5":
                square(a, b)
            elif operator == "6":
                calculator()


main()