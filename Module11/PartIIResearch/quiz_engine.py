import json
from collections import Counter

def load_questions(filename):
    with open(filename, "r") as file:
        return json.load(file)

def display_result(scores):
    most_common = Counter(scores).most_common(1)[0][0]
    print("\n Your personality type is:", most_common)
    print("\nResults breakdown:")
    for trait, score in scores.items():
        print(f"{trait}: {score}")

def run_quiz():
    questions = load_questions("questions.json")
    if not questions:
        print("No questions found.")
        return

    scores = { "Thinker": 0, "Socialite": 0, "Adventurer": 0, "Innovator": 0 }

    for q in questions:
        print("\n" + q["question"])
        for key, value in q["options"].items():
            print(f"  {key}) {value['text']}")

        answer = input("Your choice: ").lower()
        while answer not in q["options"]:
            answer = input("Invalid choice. Try again: ").lower()

        personality = q["options"][answer]["personality"]
        scores[personality] += 1

    display_result(scores)
