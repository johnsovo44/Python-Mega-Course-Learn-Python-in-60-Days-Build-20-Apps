file_path_global = 'todo_app/todos.txt'  # Create a file path for the todo list file. This combines the base directory with the file name.


def get_todos(filepath_func = file_path_global):
    """
    This function reads the todo list from a file and returns it as a list of strings.
    It opens the file in read mode, reads all lines, and returns them as a list.
    """
    with open(filepath_func,'r') as file_local:
        todolist_local = file_local.readlines()
    return todolist_local

def write_todos(todos_arg, filepath_func = file_path_global):
    """
    This function writes the todo list to a file.
    It opens the file in write mode and writes the list of todos to the file.
    """
    with open(filepath_func, 'w') as file_local:
        file_local.writelines(todos_arg)  # Write the todo list to a file named 'todos.txt'. This is a file object method that writes the list to the file.

