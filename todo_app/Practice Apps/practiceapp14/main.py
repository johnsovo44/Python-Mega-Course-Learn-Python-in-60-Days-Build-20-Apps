# this app will demonstrate decoupling the code into functions.
# decoupling is the process of separating code into smaller, independent pieces that can be reused and tested independently. This makes the code more modular and easier to maintain.

from modules.parser import parse
from modules.converter import convert
feet_inches = input("Enter your height in feet and inches (e.g., 5 12): ")


f, i = parse(feet_inches)
    
result = convert(f,i)
print("feet-inches", f, i)

if result > 1:
    print("Kid is too small")
else:
    print("Kid can use the slide")