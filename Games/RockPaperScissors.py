import random

predefined_values = {
    "1": "Rock",
    "2": "Paper",
    "3": "Scissors"
}

while True:
    system_value = str(random.randint(1, len(predefined_values)))

    print("Choose Rock/Paper/Scissors:\n")

    for v in predefined_values:
        print(f"({v}) {predefined_values[v]}")

    print(f"(q) to Quit")

    user_selection = input("\n").strip()

    if user_selection.lower() == 'q':
        print("Quitting the Game")
        break

    if user_selection not in predefined_values:
        print("\n\nPlease enter a valid value\n")
        continue

    if user_selection == system_value:
        print("\n\nIt's a tie\n")
        continue
    elif user_selection == "1" and system_value == "2":
        print(
            f"You Lose, (Your choise = {predefined_values["1"]} and System choise = {predefined_values["2"]}")
        break
    elif user_selection == "1" and system_value == "3":
        print(
            f"You Win, (Your choise = {predefined_values["1"]} and System choise = {predefined_values["3"]}")
        break
    elif user_selection == "2" and system_value == "1":
        print(
            f"You Win, (Your choise = {predefined_values["2"]} and System choise = {predefined_values["1"]}")
        break
    elif user_selection == "2" and system_value == "3":
        print(
            f"You Lose, (Your choise = {predefined_values["2"]} and System choise = {predefined_values["3"]}")
        break
    elif user_selection == "3" and system_value == "1":
        print(
            f"You Lose, (Your choise = {predefined_values["3"]} and System choise = {predefined_values["1"]}")
        break
    elif user_selection == "3" and system_value == "2":
        print(
            f"You Win, (Your choise = {predefined_values["3"]} and System choise = {predefined_values["2"]}")
        break
