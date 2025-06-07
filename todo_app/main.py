from modules import functions

# This is the main script for a simple todo application.

# Below we use a variable to store the user input for a todo item.
# A variable is a named storage location in memory that can hold data.
user_prompt = "Type add, show, edit, complete or exit:"  # This is a prompt for the user to enter a todo item. Data Type is a string.


while True:
    user_action = input(user_prompt)  # Get user input for a todo item. Data Type is a string.
    user_action = user_action.strip()

# We had match here, but it doesn't work well with 'in' statements, so we use a series of if-elif-else statements instead.

    if user_action.startswith('add'): # If the user input is "add", we proceed to add a todo item.
        todo = user_action[4:] + '\n' #list slicing
        todolist = functions.get_todos()  # Call the function to get the current todo list.
        todolist.append(todo)  # Add the todo item to the list using a list object method. This modifies the list in place.

        functions.write_todos(todolist)  # Call the function to write the updated todo list to the file.

    elif user_action.startswith('show'):  # If the user input is "show" or "display", we display the todo list.
        todolist = functions.get_todos() 

        new_todos = [item.strip('\n') for item in todolist if item]
        # Create a new list of todos by stripping the newline character from each item in the todo list.

        print("Your todo list:")  # Print a header for the todo list.
        for index, item in enumerate(new_todos):  # Iterate over each item in the todo list.
            item = item.title()
            print(f"{index + 1}. {item}")  # Print each item in the todo list with its number. The f-string is used to format the output.

    elif user_action.startswith('edit'): # If the user input is "edit", we allow the user to edit a todo item.
        try:
            todolist = functions.get_todos() 

            for index, item in enumerate(todolist):
                item = item.strip('\n').title()
                print(f"{index + 1}. {item}")

            number = int(user_action[5:])  # Extract the number from the user input to identify which todo item to edit.
            number = number - 1
            existing_todo = todolist[number]

            new_todo = input("Enter new todo item: ")
            todolist[number] = new_todo +'\n' # Update the todo item in the list with the new value.
            
            print(f"Updated todo item: {new_todo.title()}")  # Print the updated todo item to the user.

            functions.write_todos(todolist)

        except ValueError:
            print("Your command is not valid.")
            continue

    elif user_action.startswith('complete'):

        try:

            todolist = functions.get_todos() 

            for index, item in enumerate(todolist):
                item = item.strip('\n').title()
                print(f"{index + 1}. {item}")

            number = int(user_action[9:])  # Extract the number from the user input to identify which todo item is completed.
            number = number - 1  # Adjust the number to match the list index (0-based index).

            if 0 < number <= len(todolist):  # Check if the number is within the valid range of the todo list.
                completed_todo = todolist.pop(number)  # Remove the completed todo item from the list using pop method.
                print(f"Completed todo item: {completed_todo.title()}")  # Print the completed todo item to the user.
            else:
                print("Invalid number. Please try again.")  # Notify the user if the number is invalid.
            
            functions.write_todos(todolist)
        
        except IndexError:
            print("Your command is out of range. Please try again.")  # Notify the user if the index is out of range.
            continue
        
    elif user_action.startswith('exit'):
        break  # If the user input is "exit", we break out of the loop to end the program.
    
    else:  # If the user input is not recognized, we notify the user.
        print("Command not recognized. Please type 'add' to add a todo item or 'show' to display the todo list. Type exit to terminate the program.")  # Notify the user that the command is not recognized.


print ("Goodbye!")  # Print a goodbye message when the program ends. This is the final output to the user.

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