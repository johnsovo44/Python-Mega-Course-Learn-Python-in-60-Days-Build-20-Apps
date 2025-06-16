import FreeSimpleGUI as sg
from zipcreator import make_archive

label1 = sg.Text("Select files to Compress:")
input1 = sg.Input(key="-IN-")
choose_button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input(key="-IN-")
choose_button2 = sg.FolderBrowse("Choose", key="folder")

output_label = sg.Text(key="output_label", size=(40, 1), text_color="green")

window = sg.Window("File Compressor", 
                   layout=[ [label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [sg.Button("Exit"), sg.Button("Compress"), output_label]],
                    font=("Helvetica", 12))

while True:
        events, values = window.read()
        print(events, values)
        filepaths = values["files"].split(";")
        folder = values["folder"]
        make_archive(filepaths, folder)
        window["output_label"].update(value= "Files compressed successfully!")

window.close()