questions = [
    {
        "question": "What is full form of DPU?",
        "options": [
            {"value": "a", "label": "Display Program Unit"},
            {"value": "b", "label": "Digital Printout Utilizer"},
            {"value": "c", "label": "Data Processing Unit"},
            {"value": "d", "label": "Dumpster Pallet Utilizer"},
        ],
        "correct_answer": "c"
    },
    {
        "question": "What is full form of CPU?",
        "options": [
            {"value": "a", "label": "Charging Programatic Universe"},
            {"value": "b", "label": "Central Processing Unit"},
            {"value": "c", "label": "Common Program Utilizer"},
            {"value": "d", "label": "Color Pallet Utilizer"},
        ],
        "correct_answer": "b"
    },
    {
        "question": "What is full form of GPU?",
        "options": [
            {"value": "a", "label": "Graphics Processing Unit"},
            {"value": "b", "label": "Granted Permission Utilizer"},
            {"value": "c", "label": "Gotcha Processing Unit"},
            {"value": "d", "label": "Granted Pallet Utilizer"},
        ],
        "correct_answer": "a"
    }
]

correct_answers = incorrect_answers = 0

for question in questions:
    print(question["question"])

    for option in question["options"]:
        print(f"({option["value"].upper()}) {option["label"]}")

    answer = input("\nPlease choose you Answer = ")
    if (answer.lower() == question["correct_answer"]):
        correct_answers += 1
        print("\n... Correct ...\n")
    else:
        incorrect_answers += 1
        print("\nxxx --- Incorrect --- xxx\n")


print(
    f"\nYou have Gussed {correct_answers} Correct Answers and {incorrect_answers} Incorrect Answers\n")
