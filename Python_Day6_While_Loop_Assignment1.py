# 1.Write a python program to check whether a number is palindrome or not? 

# Function to check if a number is a palindrome
def is_palindrome(number):
    # Convert the number to a string to check the palindrome property
    number_str = str(number)
    
    # Reverse the string and compare it to the original
    reversed_str = number_str[::-1]
    
    # If the original string is equal to its reversed version, it's a palindrome
    if number_str == reversed_str:
        return True  # Return True if the number is a palindrome
    else:
        return False  # Return False if the number is not a palindrome

# Take input from the user
num = int(input("Enter a number: "))

# Check if the number is a palindrome
if is_palindrome(num):
    print(f"{num} is a palindrome.")  # Print if the number is a palindrome
else:
    print(f"{num} is not a palindrome.")  # Print if the number is not a palindrome


# Answer:-
""" Enter a number: 5
5 is a palindrome. """
