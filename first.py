import random

print("=== Number Guessing Game ===")

lower = 1
upper = 100

secret = random.randint(lower, upper)
attempts = 0

print(f"Guess the number between {lower} and {upper}")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret:
        print("Try a Higher Number.")
    elif guess > secret:
        print("Try a Lower Number.")
    else:
        print("Correct!")
        print("Total Attempts:", attempts)
        break