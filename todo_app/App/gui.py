import modules.functions as functions

# we could use tkinter, but we will use a more advanced GUI Library
import FreeSimpleGUI as gui

label = gui.Text('Welcome to My To-Do App!')
input_box = gui.InputText(tooltip= 'Enter a task', key='Added Task')
add_button = gui.Button('Add')

window = gui.Window('My To-Do App', 
                    layout=[[label], [input_box, add_button]],
                    font=("Helvetica", 20)
        )

while True:
    
        event, values = window.read()
# this actually returns a tuple with the event and values
# the key I added in the input box is used to get the value

        match event:
                case "Add":
                        todos = functions.get_todos()
                        new_todo = values['Added Task'] + '\n'
                        todos.append(new_todo)
                        functions.write_todos(todos)
                        window['Added Task'].update('')  
                        # Clear the input box after adding
                case gui.WIN_CLOSED:
                        break

window.close()