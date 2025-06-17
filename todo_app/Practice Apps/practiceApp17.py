import FreeSimpleGUI as gui

add_button = gui.Button(size=2, image_source='todo_app/Practice Apps/files/add.png', mouseover_colors=('lightblue2'), tooltip='Add a task', key='Add')
edit_button = gui.Button('Edit')
complete_button = gui.Button('Complete')
exit_button = gui.Button('Exit')

window = gui.Window('My To-Do App',
                    layout=[[add_button],
                            [edit_button, complete_button],
                            [exit_button]],
                    font=("Helvetica", 20)
        )

window.read()  # Read the window to initialize it
while True:
    event, values = window.read(timeout=200)
    print(event, values)  # Print the event and values for debugging

    match event:
        case "Add":
            gui.popup("Add button clicked", font=("Helvetica", 20))
        case "Edit":
            gui.popup("Edit button clicked", font=("Helvetica", 20))
        case "Complete":
            gui.popup("Complete button clicked", font=("Helvetica", 20))
        case "Exit" | gui.WIN_CLOSED:
            break