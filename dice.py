import random

print("=== Dice Rolling Simulator ===")

sides = int(input("Number of sides on the dice: "))

while True:
    result = random.randint(1, sides)
    print("You rolled:", result)

    again = input("Roll again? (y/n): ").lower()

    if again != "y":
        print("Game Over")
        break