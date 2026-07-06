print("=== Mad Libs Story ===")

name = input("Enter a person's name: ")
place = input("Enter a place: ")
animal = input("Enter an animal: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")

story = f"""
One day, {name} went to {place}.
There, a {adjective} {animal} suddenly appeared.
Without thinking twice, it started to {verb}.
Everyone laughed, and the day became unforgettable.
"""

print("\nGenerated Story")
print(story)