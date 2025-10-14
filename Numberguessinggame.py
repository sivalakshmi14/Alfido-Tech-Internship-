# Task 2: Number Guessing Game
import random

print("=== Number Guessing Game ===")
print("Guess the number between 1 and 100")

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! You guessed the number {number} in {attempts} attempts.")
        break
