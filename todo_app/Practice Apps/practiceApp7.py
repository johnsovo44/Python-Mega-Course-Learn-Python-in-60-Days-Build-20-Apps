contents = ["All carrots are red",
             "All apples are green",
               "All bananas are yellow"]

filenames = ["carrot.txt",
              "apple.txt",
                "banana.txt"]

for content, filename in zip(contents, filenames): #zip combines the contents and filenames lists into pairs.
    with open(f"todo_app/Practice Apps/files/{filename}", "w") as file:
        file.write(content)