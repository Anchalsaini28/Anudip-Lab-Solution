# 2. Python program to check if a given number is an Armstrong number

# Function to check if a given number is an Armstrong number
def is_armstrong(number):
    # Convert the number to a string to easily iterate over each digit
    num_str = str(number)
    
    # Find the number of digits in the number
    num_digits = len(num_str)
    
    # Initialize the sum of powers of digits to zero
    sum_of_powers = 0
    
    # Iterate over each digit in the number
    for digit in num_str:
        # Convert the digit back to an integer and raise it to the power of the number of digits
        # Add the result to the sum_of_powers
        sum_of_powers += int(digit) ** num_digits
    
    # Check if the sum of powers is equal to the original number
    if sum_of_powers == number:
        # If true, the number is an Armstrong number
        return True
    else:
        # If false, the number is not an Armstrong number
        return False

# Input: Prompt the user to enter a number
user_input = int(input("Enter a number to check if it's an Armstrong number: "))

# Call the function with the user's input and store the result
if is_armstrong(user_input):
    # Print confirmation if the number is an Armstrong number
    print(f"{user_input} is an Armstrong number.")
else:
    # Print confirmation if the number is not an Armstrong number
    print(f"{user_input} is not an Armstrong number.")

# Answer:-
""" Enter a number to check if it's an Armstrong number: 153
153 is an Armstrong number.
"""

# 2.1. Python program to check if a given number is not an Armstrong number


# Function to check if a given number is an Armstrong number
def is_armstrong(number):
    # Convert the number to a string to easily iterate over each digit
    num_str = str(number)
    
    # Find the number of digits in the number
    num_digits = len(num_str)
    
    # Initialize the sum of powers of digits to zero
    sum_of_powers = 0
    
    # Iterate over each digit in the number
    for digit in num_str:
        # Convert the digit back to an integer and raise it to the power of the number of digits
        # Add the result to the sum_of_powers
        sum_of_powers += int(digit) ** num_digits
    
    # Check if the sum of powers is equal to the original number
    if sum_of_powers == number:
        # If true, the number is an Armstrong number
        return True
    else:
        # If false, the number is not an Armstrong number
        return False

# Input: Prompt the user to enter a number
user_input = int(input("Enter a number to check if it's an Armstrong number: "))

# Call the function with the user's input and store the result
if is_armstrong(user_input):
    # Print confirmation if the number is an Armstrong number
    print(f"{user_input} is an Armstrong number.")
else:
    # Print confirmation if the number is not an Armstrong number
    print(f"{user_input} is not an Armstrong number.")


# Answer:-
""" Enter a number to check if it's an Armstrong number: 145
145 is not an Armstrong number.
"""

