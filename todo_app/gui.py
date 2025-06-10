import modules.functions as functions

# we could use tkinter, but we will use a more advanced GUI Library
import FreeSimpleGUI as gui

label = gui.Text('Welcome to My To-Do App!')
input_box = gui.InputText(tooltip= 'Enter a task')
add_button = gui.Button('Add')

window = gui.Window('My To-Do App', layout=[
        [label], 
        [input_box, add_button]
        ]
        )
window.read()
window.close()