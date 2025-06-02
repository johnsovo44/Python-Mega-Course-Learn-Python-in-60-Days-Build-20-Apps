try:
    width = float(input("Enter the width of the rectangle: "))
    length = float(input("Enter the length of the rectangle: "))

    if width == length:
        exit("This is a square, not a rectangle.")
        #the exit function is used to terminate the program if the condition is met.
    area = width * length
    print(f"The area of the rectangle is: {area}")
except ValueError:
    print("Invalid input. Please enter numeric values for width and length.")

    """
    This code snippet calculates the area of a rectangle based on user input for width and length.
    """