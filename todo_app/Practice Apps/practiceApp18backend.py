import zipfile

def extract_archive(archive_path, dest_dir):
    """Extracts a zip archive to a specified directory."""
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    extract_archive("C:/Users/vonnj/Coding Projects/Python Mega Course Learn Python in 60 Days Build 20 Apps/todo_app/Practice Apps/files/compressed.zip", "C:/Users/vonnj/Coding Projects/Python Mega Course Learn Python in 60 Days Build 20 Apps/todo_app/Practice Apps/dest")