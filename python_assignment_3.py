"""
Python Assignment 3: While Loop, For Loop and Function
"""

import random


# ---------------------------------------------------------------
# 1. WHILE LOOP & CONTROL STATEMENTS: Number Guessing Game
# ---------------------------------------------------------------
def number_guessing_game():
    print("=== Number Guessing Game ===")

    # Generate random number between 1 and 10
    secret_number = random.randint(1, 10)

    # Maximum number of guesses allowed
    attempts = 3

    while attempts > 0:
        guess = int(input("Guess the number (between 1 and 10): "))

        # Out of range: inform the user and skip the rest of the loop
        # (this does not use up an attempt)
        if guess < 1 or guess > 10:
            print("Your guess is out of range. Please guess a number between 1 and 10.")
            continue

        # A valid guess uses up one attempt
        attempts -= 1

        if guess == secret_number:
            print("Congratulations! You guessed the correct number.")
            break  # exit the loop when the guess is correct
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print("Too low. Try again.")
    else:
        # Runs only if the loop ended without 'break' (attempts ran out)
        print("Better luck next time! The number was", secret_number)


# ---------------------------------------------------------------
# 2. FOR LOOP: Multiplication Table Generator
# ---------------------------------------------------------------
def multiplication_table():
    print("\n=== Multiplication Table Generator ===")

    number = int(input("Enter the number for which you want the multiplication table: "))

    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")


# ---------------------------------------------------------------
# 3. FUNCTION: BMI Calculator
# ---------------------------------------------------------------
def calculate_bmi(weight, height):
    """Return BMI = weight (kg) / height (m) squared."""
    return weight / (height ** 2)


def bmi_calculator():
    print("\n=== BMI Calculator ===")

    weight = float(input("Enter your weight in kg: "))
    height = float(input("Enter your height in meters: "))

    bmi = calculate_bmi(weight, height)
    print(f"Your BMI is: {bmi:.2f}")


# ---------------------------------------------------------------
# Run all three programs
# ---------------------------------------------------------------
number_guessing_game()
multiplication_table()
bmi_calculator()
