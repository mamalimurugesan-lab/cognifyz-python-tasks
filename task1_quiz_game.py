# Cognifyz Task 1 - Basic Text-Based Quiz Game

print("=" * 45)
print("        GENERAL KNOWLEDGE QUIZ")
print("=" * 45)

questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Chennai", "D. Kolkata"],
        "answer": "B"
    },
    {
        "question": "2. Which language is used to create web pages?",
        "options": ["A. HTML", "B. Python", "C. SQL", "D. C"],
        "answer": "A"
    },
    {
        "question": "3. What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Personal Unit",
            "C. Central Program Utility",
            "D. Control Processing User"
        ],
        "answer": "A"
    },
    {
        "question": "4. Which data type stores True or False?",
        "options": ["A. String", "B. Integer", "C. Boolean", "D. Float"],
        "answer": "C"
    },
    {
        "question": "5. Which symbol is used for comments in Python?",
        "options": ["A. //", "B. #", "C. /* */", "D. --"],
        "answer": "B"
    }
]

score = 0

for item in questions:
    print("\n" + item["question"])
    for option in item["options"]:
        print(option)

    answer = input("Enter your answer (A/B/C/D): ").strip().upper()

    if answer == item["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! Correct answer:", item["answer"])

print("\n" + "=" * 45)
print(f"Quiz completed! Your score: {score}/{len(questions)}")

if score == len(questions):
    print("Excellent!")
elif score >= 3:
    print("Good job!")
else:
    print("Keep practicing!")
print("=" * 45)
