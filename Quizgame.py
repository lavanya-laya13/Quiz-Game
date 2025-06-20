# quiz_game.py

def welcome():
    print("Welcome to the Python Quiz Game!")
    print("You'll be asked 5 questions. Try to answer them all correctly.")
    print("Let's begin!\n")


def ask_question(question, options, correct_option):
    print(question)
    for key in options:
        print(f"{key}. {options[key]}")
    answer = input("Your answer (A/B/C/D): ").upper()
    if answer == correct_option:
        print("✅ Correct!\n")
        return True
    else:
        print(f"❌ Wrong! The correct answer was {correct_option}.\n")
        return False


def run_quiz():
    score = 0
    questions = [
        {
            "question": "What is the capital of France?",
            "options": {"A": "Berlin", "B": "Madrid", "C": "Paris", "D": "Rome"},
            "answer": "C"
        },
        {
            "question": "Which language is primarily used for web development?",
            "options": {"A": "Python", "B": "HTML", "C": "C++", "D": "Java"},
            "answer": "B"
        },
        {
            "question": "Who developed the theory of relativity?",
            "options": {"A": "Isaac Newton", "B": "Einstein", "C": "Tesla", "D": "Darwin"},
            "answer": "B"
        },
        {
            "question": "What does CPU stand for?",
            "options": {"A": "Central Power Unit", "B": "Central Processing Unit", "C": "Computer Power Unit", "D": "Control Processing Unit"},
            "answer": "B"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": {"A": "Earth", "B": "Jupiter", "C": "Mars", "D": "Venus"},
            "answer": "C"
        },
    ]

    for q in questions:
        if ask_question(q["question"], q["options"], q["answer"]):
            score += 1

    print(f"🎉 You got {score} out of {len(questions)} questions right!")

    if score == len(questions):
        print("Excellent job! 🏆")
    elif score >= 3:
        print("Good effort! 👍")
    else:
        print("Better luck next time! 💡")


if __name__ == "__main__":
    welcome()
    run_quiz()
