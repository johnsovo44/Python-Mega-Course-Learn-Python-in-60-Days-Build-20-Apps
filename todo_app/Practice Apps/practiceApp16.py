import FreeSimpleGUI as sg

label1 = sg.Text("Select files to Compress:")
input1 = sg.Input(key="-IN-")
choose_button1 = sg.FilesBrowse("Choose", key="-BROWSE-")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input(key="-IN-")
choose_button2 = sg.FolderBrowse("Choose", key="-BROWSE-")

window = sg.Window("File Compressor", 
                   layout=[ [label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [sg.Button("Compress"), sg.Button("Exit")]],
                    font=("Helvetica", 12))

window.read()
window.close()