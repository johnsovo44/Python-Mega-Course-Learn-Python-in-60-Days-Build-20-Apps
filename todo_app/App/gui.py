import modules.functions as functions

# we could use tkinter, but we will use a more advanced GUI Library
import FreeSimpleGUI as gui

import time

gui.theme('Dark')  # Set the theme for the GUI

label_time = gui.Text('', key = 'time')
label = gui.Text('Welcome to My To-Do App!')
input_box = gui.InputText(tooltip= 'Enter a task', key='Added Task')
add_button = gui.Button('Add', size = 10, image_source='add.png')
list_box = gui.Listbox(values=functions.get_todos(),
                      key='Todos',
                      enable_events=True,
                      size=[45, 10])  # Enable events to update the list box
edit_button = gui.Button('Edit')
complete_button = gui.Button('Complete')
exit_button = gui.Button('Exit')

window = gui.Window('My To-Do App', 
                    layout=[[label_time],
                            [label],
                             [input_box, add_button],
                               [list_box, edit_button, complete_button],
                               [exit_button]],
                    font=("Helvetica", 20)
        )

while True:
    
        event, values = window.read(timeout=200)
        window['time'].update(value=time.strftime('%b %d, %Y %H:%M:%S'))  # Update the time label
        print(1, event)
        print(2, values)
        print(3, values['Added Task'])
        print(4, values['Todos'])
# this actually returns a tuple with the event and values
# the key I added in the input box is used to get the value

        match event:
                case "Add":
                        todos = functions.get_todos()
                        new_todo = values['Added Task'] + '\n'
                        todos.append(new_todo)
                        functions.write_todos(todos)
                        window['Todos'].update(values=todos)
                        window['Added Task'].update('')  
                        # Clear the input box after adding

                case "Edit":
                        try:
                                todo_to_edit = values['Todos'][0]  # Get the selected todo
                                new_todo = values['Added Task'] + '\n'
                                todos = functions.get_todos()
                                index = todos.index(todo_to_edit)  # Find the index of the selected todo
                                todos[index] = new_todo  # Update the todo at the index
                                functions.write_todos(todos)
                                window['Todos'].update(values=todos)
                                window['Added Task'].update('')  # Clear the input box after editing
                        except IndexError:
                                gui.popup("Please select a item first", font=("Helvetica", 20))

                case "Complete":
                        try:
                                todo_to_complete = values['Todos'][0]
                                todos = functions.get_todos()
                                todos.remove(todo_to_complete)  # Remove the completed todo
                                functions.write_todos(todos)
                                window['Todos'].update(values=todos)
                                window['Added Task'].update('')  # Clear the input box after completing
                        except IndexError:
                                gui.popup("Please select a item first", font=("Helvetica", 20))
                
                case "Exit":
                        break  # Exit the loop and close the window

                case 'Todos':
                        window['Added Task'].update(value = values['Todos'][0].strip())

                case gui.WIN_CLOSED:
                        break # stops the loop not the program

window.close()