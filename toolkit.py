# Personal Mini-Toolkit
# This program contains a calculator, a to-do list, and a number guessing game.

import random

# Tool 1: Calculate the result of a basic arithmetic operation.
def calculator():
    print("\n--- Simple Calculator ---")

    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Sorry, you cannot divide by zero.")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please use +, -, *, or /.")
            return

        print(f"The result is: {result}")

    except ValueError:
        print("Please enter valid numbers.")

# Tool 2: Add, view, and remove tasks from a changing list.
def todo_list():
    tasks = []

    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            task = input("Enter your task: ").strip()

            if task:
                tasks.append(task)
                print(f"Task added: {task}")
            else:
                print("A task cannot be empty.")

        elif choice == "2":
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if not tasks:
                print("There are no tasks to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    task_number = int(
                        input("Enter the task number to remove: ")
                    )

                    if 1 <= task_number <= len(tasks):
                        removed = tasks.pop(task_number - 1)
                        print(f"Removed task: {removed}")
                    else:
                        print("That task number does not exist.")

                except ValueError:
                    print("Please enter a valid whole number.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 4.")

# Tool 3: Give hints until the user guesses the secret number.
def guessing_game():
    secret_number = random.randint(1, 10)
    attempts = 0

    print("\n--- Number Guessing Game ---")
    print("I am thinking of a number between 1 and 10.")
    print("Enter 0 if you want to stop playing.")

    while True:
        try:
            guess = int(input("Your guess: "))

            if guess == 0:
                print("You left the game. Thanks for playing!")
                break

            if guess < 1 or guess > 10:
                print("Please choose a number between 1 and 10.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(
                    f"Correct! You guessed it in {attempts} attempts."
                )
                break

        except ValueError:
            print("Please enter a whole number.")

# Main menu: Repeat until the user chooses to quit.
def main():
    print("Welcome to my Personal Mini-Toolkit!")

    while True:
        print("\n====================================")
        print("   WELCOME TO MY PERSONAL TOOLKIT!")
        print("====================================")
        print("1. Simple Calculator")
        print("2. To-Do List")
        print("3. Number Guessing Game")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            calculator()
        elif choice == "2":
            todo_list()
        elif choice == "3":
            guessing_game()
        elif choice == "4":
            print(
                "Thank you for using my Personal Mini-Toolkit. Goodbye!"
            )
            break
        else:
            print(
                "Sorry, that choice is not on the menu. "
                "Please enter a number from 1 to 4."
            )

# Start the program.
if __name__ == "__main__":
    main()