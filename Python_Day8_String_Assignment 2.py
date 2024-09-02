# 2. Write a Python program to remove a newline in Python
# String = "\nBest \nDeeptech \nPython \nTraining\n"

# Define the string with newline characters
string_with_newlines = "\nBest \nDeeptech \nPython \nTraining\n"

# Step 1: Use the `strip` method to remove leading and trailing whitespace, including newlines
string_no_newlines = string_with_newlines.strip()

# Step 2: Replace any remaining newline characters with a space or remove them entirely
# Using `replace` method to remove all newline characters
string_cleaned = string_no_newlines.replace('\n', ' ')

# Step 3: Print the cleaned string to display the result
print("Cleaned String:")
print(string_cleaned)

# Answer:-

"""
Cleaned String:
Best  Deeptech  Python  Training

"""
