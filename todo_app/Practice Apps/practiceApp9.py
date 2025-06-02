date_ = input("Enter date (YYYY-MM-DD): ")
mood = input("Enter mood: ")
journal = input("Enter journal entry:\n")

with open(f"todo_app/Practice Apps/journal/{date_}.txt", "w") as file:
    file.write(mood + 2 * "\n") 
    file.write(journal)
    print(f"Journal entry for {date_} saved successfully.")