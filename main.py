import json

with open("task.json", "r") as file:
    task = json.load(file)

def main():
    while True:
        command = input("task-tracker> ")

        if command == "exit":
            print("Programm beendet")
            break

        elif command == "add":
            user_input = input ("Neue Aufgabe hinzufügen: ")
            task.append(user_input)

            with open("task.json", "w") as file:
                json.dump(task, file, indent=4)

            print("Wurde hinzugefügt:", user_input)

        elif command == "list":
            print("Liste:", task)

        else:
            print("Ungültige Eingabe: ")


if __name__ == "__main__":
    main()