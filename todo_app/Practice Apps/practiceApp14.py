# this app will demonstrate decoupling the code into functions.
# decoupling is the process of separating code into smaller, independent pieces that can be reused and tested independently. This makes the code more modular and easier to maintain.

feet_inches = input("Enter your height in feet and inches (e.g., 5 12): ")

def parse(feet_inches_local):
    parts = feet_inches_local.split(" ")  # Split the input string into a list of strings.
    feet = float(parts[0])
    inches = float(parts[1]) 
    return feet, inches  # Return the feet and inches as a tuple.

def convert(feet, inches):
    """
    Convert height from feet and inches to meters.
    """

    meters = feet * 0.3048 + inches * 0.0254
    return meters

f, i = parse(feet_inches)
    
result = convert(f,i)
print("feet-inches", f, i)

if result > 1:
    print("Kid is too small")
else:
    print("Kid can use the slide")