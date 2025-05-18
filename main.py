# Practice for addition, subtraction, multiplication, and division.

from random import randint
import os


def clear():
    """Clear the screen."""
    os.system("cls")


def rounded(x):
    """Round x to the nearest tenth."""
    return round(10 * x) / 10


def addition(a, b):
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


def subtraction(a, b):
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


def multiplication(a, b):
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


def division(a, b):
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
        # Obtain the expression from the user.
        expression = input()
        clear()

        # Check if the user wants to go back.
        if expression == "":
            break

        # Calculate the expression.
        try:
            answer = eval(expression)
            print(f"{expression} = \033[32m{answer}\033[0m")
            input()
            clear()
        except:
            clear()
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
        if b == "":
            continue

        # Initialize the loop.
        operation = " "

        while operation != "":
            # Choose an operation.
            print("(1) Addition")
            print("(2) Subtraction")
            print("(3) Multiplication")
            print("(4) Division")
            print("(5) Square")
            print("(6) Calculator\n")
            operation = input("Input: ")
            clear()

            # Run the operation program
            if operation == "1":
                addition(a, b)
            elif operation == "2":
                subtraction(a, b)
            elif operation == "3":
                multiplication(a, b)
            elif operation == "4":
                division(a, b)
            elif operation == "5":
                square(a, b)
            elif operation == "6":
                calculator()


main()