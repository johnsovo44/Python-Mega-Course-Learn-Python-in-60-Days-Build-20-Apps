"""
Notes: 
- Command line is used to interact with a script via text input and output.
- You want to follow the input-processing-output pattern. The input is the input from the user, the processing is the logic of the script, and the output is what is displayed to the user. 
- In the case of the to do list app, the input is the user's command (like adding a task), the processing is the logic to add that task to the list, and the output is the updated list of tasks.
- main.py is the entry point of the application, where the main logic is executed.
- remember to be literal when naming your variables, functions, and files. Makes readability of your code easier for future you and others.
- Using intermediate variables, aka variables you don't need but are used to make the code more readable, is a good practice.

Concepts Used in this Script:
- Strings
- Variables
- main.py
- input function
"""
# This is the main script for a simple todo application.

# Below we use a variable to store the user input for a todo item.
# A variable is a named storage location in memory that can hold data.
user_prompt = "Enter todo:"  # This is a prompt for the user to enter a todo item. Data Type is a string.

todo1 = input(user_prompt)  # Get user input for the todo item
todo2 = input(user_prompt)
todo3 = input(user_prompt)
# you can place text inside the input function to prompt the user.

print("adding todo...")  # Notify the user that the todo is being added
# Here we simulate adding the todo item to a list.

todos = [todo1, todo2, todo3]  # Initialize an empty list to store todo items. Data Type is a list.
# A list is a collection of items that can be of any data type, including strings, integers, or even other lists.

print(f"Your todo list: {todos}")  # Notify the user that the todo list is being displayed