filenames = ["1.Raw Data.txt", "2.Processed Data.txt", "3.Report.txt"]
item = 0

for filename in filenames:
    filename = filename.replace(".", "-",1)
    filenames[item] = filename
    item += 1
print(filenames)

# Strings are immutable, meaning they cannot be changed in place.
# However, we can create a new string with the desired changes and assign it back to the variable.
# List are mutable, meaning they can be changed in place.
# In this case, we are replacing the first occurrence of "." with "-" in each filename.
# Why are list mutable and strings immutable?
# Lists are mutable because they are designed to hold a collection of items that can change over time, such as adding or removing items.
# Strings are immutable because they are designed to hold a single piece of text that does not change, ensuring that the original string remains unchanged.
# This immutability allows for better performance and memory management in Python.