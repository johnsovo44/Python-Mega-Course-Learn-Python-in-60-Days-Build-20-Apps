def greet():
    """
    Always write a definition for your functions.
    """
    message = "Hello, welcome to the practice app!"
    print("hey hey")
    new_message = message.replace("Hello", "Hi")
    return new_message # if this isn't here it will return None object
# don't confuse return with print.

greeting = greet()
print(greeting)