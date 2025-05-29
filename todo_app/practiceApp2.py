password = input("Enter your password: ")

while password != "pass123":
    print("Incorrect password. Please try again.")
    password = input("Enter your password: ")

print("Password accepted. Welcome!")  # Notify the user that the password is accepted
# This script prompts the user for a password and checks if it matches a predefined password.