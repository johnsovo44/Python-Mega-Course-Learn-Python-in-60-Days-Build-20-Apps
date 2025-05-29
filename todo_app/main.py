"""
Notes: 
- Command line is used to interact with a script via text input and output.
- You want to follow the input-processing-output pattern. The input is the input from the user, the processing is the logic of the script, and the output is what is displayed to the user. 
- In the case of the to do list app, the input is the user's command (like adding a task), the processing is the logic to add that task to the list, and the output is the updated list of tasks.
- main.py is the entry point of the application, where the main logic is executed.
- remember to be literal when naming your variables, functions, and files. Makes readability of your code easier for future you and others.
- Using intermediate variables, aka variables you don't need but are used to make the code more readable, is a good practice.
- Python is a language and your computer speaks a language called machine code. When you install python you really are installing CPython, an interpreter that translates python code, which comes off as english, into C the language that your computer understands. It outputs the C language back into python for you to read and understand it.

Concepts Used in this Script:
- Strings
- Variables
- main.py
- input function
"""
# This is the main script for a simple todo application.

# Below we use a variable to store the user input for a todo item.
# A variable is a named storage location in memory that can hold data.
user_prompt = "Type add or show or exit:"  # This is a prompt for the user to enter a todo item. Data Type is a string.

todolist = []  # Initialize an empty list to store todo items. Data Type is a list.
while True:
    user_action = input(user_prompt)  # Get user input for a todo item. Data Type is a string.
    user_action = user_action.strip()

    match user_action:  # Check the user input against the expected commands.
        case "add": # If the user input is "add", we proceed to add a todo item.
            todo = input("Enter a todo item: ")  # Get the todo item from the user. Data Type is a string.
            todolist.append(todo)  # Add the todo item to the list using a list object method. This modifies the list in place.
        case "show" | "display":  # If the user input is "show" or "display", we display the todo list.
            print("Your todo list:")  # Print a header for the todo list.
            for item in todolist:  # Iterate over each item in the todo list.
                item = item.title()
                print(item)
        case "exit":
            break  # If the user input is "exit", we break out of the loop to end the program.
        case _:  # If the user input is not recognized, we notify the user. A variable is defined on the fly to handle text we didn't anticipate.
            print("Command not recognized. Please type 'add' to add a todo item or 'show' to display the todo list. Type exit to terminate the program.")  # Notify the user that the command is not recognized.


print ("Goodbye!")  # Print a goodbye message when the program ends. This is the final output to the user.