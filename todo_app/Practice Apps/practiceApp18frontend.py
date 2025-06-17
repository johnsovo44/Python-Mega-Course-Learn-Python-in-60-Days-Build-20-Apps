import FreeSimpleGUI as sg
from practiceApp18backend import extract_archive

sg.theme("Black")

label1 = sg.Text("Select archive: ")
input1 = sg.Input(key="archive input")
choose_button1 = sg.FileBrowse("Choose", key = "archive button")

label2 = sg.Text("Select dest dir: ")
input2 = sg.Input(key="folder input")
choose_button2 = sg.FolderBrowse("Choose", key = "folder")

extract_button = sg.Button("Extract", key = "Extract")
output_label = sg.Text(key="output", text_color = "light green")

window = sg.Window("Archive Extractor",
                   layout=[[label1, input1, choose_button1],
                           [label2, input2, choose_button2],
                           [extract_button, output_label]],
                   font=("Helvetica", 20))

while True:
        events, values = window.read()  # Read the window to initialize it
        print(events, values)
        archivepath = values["archive button"]
        destdir = values["folder input"]
        extract_archive(archivepath, destdir)
        window["output"].update(f"Extracted file to destination folder")

window.close()  # Close the window after reading