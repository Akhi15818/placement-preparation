score = 0

questions = [
    ("What is the capital of India?", "Delhi"),
    ("How many days are there in a week?", "7"),
    ("Which language is used for AI?", "Python")
]

for question, answer in questions:
    user = input(question + " ")

    if user.strip().lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong! Correct answer:", answer)

print("Your Score:", score, "/", len(questions))