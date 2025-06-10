import glob
import os

# Ensure the directory exists and use an absolute path if needed
directory = os.path.join(os.path.dirname(__file__), "Practice Apps")
myfiles = glob.glob(os.path.join(directory, "*.py"))
for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read())