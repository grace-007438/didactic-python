# Quiz Application

questions = [
    {
        "question": "Who developed Python?",
        "options": ["A. James Gosling", "B. Guido van Rossum", "C. Dennis Ritchie", "D. Bjarne Stroustrup"],
        "answer": "B"
    },
    {
        "question": "What is a name used to identify a variable, function, class, module and object in Python?",
        "options": ["A. identifier", "B. shell", "C. interpreter", "D. none of these"],
        "answer": "A"
    },
    {
        "question": "What is the keyword to define a function in Python?",
        "options": ["A. func", "B. define", "C. def", "D. function"],
        "answer": "C"
    },
    {
        "question": "What are special symbols that represent Computations?",
        "options": ["A. operators", "B. values", "C. symbols", "D. none of these"],
        "answer": "A"

    },
    {
       "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. /* */", "C. #", "D. <!-- -->"],
        "answer": "C"
    },
]

score = 0

print("===== QUIZ APPLICATION =====")

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! Correct answer is:", q["answer"])

print("\n===== QUIZ RESULT =====")
print("Total Questions:", len(questions))
print("Correct Answers:", score)
print("Your Score:", score, "/", len(questions))
