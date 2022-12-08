quiz = [
    {
        "question": "What color does blue and yellow make?",
        "choices":[
            "Banana "
            "Orange "
            "Apple "
            "Green "
        ],
        "answer": "Green"
    },
    {   
          "question": "what is the most popular fruit in the world?",
        "choices":[
            "Tomatoes "
            "Snow "
            "Apple "
            "Grapes "
        ],
        "answer": "Tomatoes"
    }
]   

problemNumber = 0
correct = 0
for problem in quiz:
    problemNumber += 1
    print(f"Question {problemNumber}: {problem['question']}")

    for choice in problem['choices']:
        print(f"  {choice}")

    guess = input("your guess: ")
    if guess == problem['answer']:
        correct += 1
        print("you = smart")
    else:
        print("you = falure ")
    print()
print(f"Correct: {correct} of {problemNumber} ({correct * 100 / problemNumber}%)")

