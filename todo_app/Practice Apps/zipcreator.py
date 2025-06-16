import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as zipf:
        
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            zipf.write(filepath, arcname=filepath.name)


if __name__ == "__main__":
    make_archive(filepaths = ["todo_app/Practice Apps/practiceApp1.py", "todo_app/Practice Apps/practiceApp2.py"],
                 dest_dir = "todo_app/Practice Apps/dest")