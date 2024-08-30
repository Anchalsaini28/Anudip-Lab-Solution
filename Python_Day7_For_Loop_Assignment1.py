# 1.Python program to check if the given string is a palindrome

# Function to check if a string is a palindrome
def is_palindrome(s):
    # Convert the string to lowercase to ignore case sensitivity
    s = s.lower()

    # Remove any non-alphanumeric characters from the string
    # This ensures that spaces, punctuation, etc., are ignored
    s = ''.join(char for char in s if char.isalnum())

    # Compare the string with its reverse
    # If both are the same, it's a palindrome
    return s == s[::-1]

# Input: Ask the user to enter a string
input_string = input("Enter a string to check if it's a palindrome: ")

# Check if the input string is a palindrome using the function
if is_palindrome(input_string):
    # If the function returns True, the string is a palindrome
    print("The given string is a palindrome.")
else:
    # If the function returns False, the string is not a palindrome
    print("The given string is not a palindrome.")

# Answer:-
"""
Enter a string to check if it's a palindrome: 8
The given string is a palindrome.
"""
