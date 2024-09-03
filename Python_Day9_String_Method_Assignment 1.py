# 1. Write a Python program to Count all letters, digits, and special symbols from the given string

# Input = “P@#yn26at^&i5ve” Output: Chars = 8 Digits = 2 Symbol = 3

# Function to count letters, digits, and special symbols in a string
def count_chars_digits_symbols(input_string):
    # Initialize counters for letters, digits, and symbols
    count_letters = 0
    count_digits = 0
    count_symbols = 0
    
    # Iterate through each character in the input string
    for char in input_string:
        # Check if the character is a letter (either uppercase or lowercase)
        if char.isalpha():
            count_letters += 1
        # Check if the character is a digit
        elif char.isdigit():
            count_digits += 1
        # If the character is neither a letter nor a digit, it's a symbol
        else:
            count_symbols += 1
    
    # Return the counts as a tuple
    return count_letters, count_digits, count_symbols

# Input string
input_string = "P@#yn26at^&i5ve"

# Get the counts
chars, digits, symbols = count_chars_digits_symbols(input_string)

# Print the results
print(f"Chars = {chars}")
print(f"Digits = {digits}")
print(f"Symbols = {symbols}")

# Answer:-

"""
Chars = 8
Digits = 3
Symbols = 4

"""
