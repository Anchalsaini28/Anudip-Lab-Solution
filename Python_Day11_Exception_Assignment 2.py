# 2. Write a Python program that prompts the user to input an integer and raises a ValueError exception if the input is not a valid integer.

def get_integer():
    try:
        # Prompt the user to input an integer
        user_input = input("Enter an integer: ")
        
        # Attempt to convert the input to an integer
        number = int(user_input)
        
        # Display the valid integer
        print(f"You entered the integer: {number}")
        
    except ValueError:
        # Raise a ValueError with a custom message if the input is not an integer
        raise ValueError("Error: The input is not a valid integer.")

# Call the function
try:
    get_integer()
except ValueError as e:
    # Catch and print the custom error message
    print(e)
    
# Answer:-

"""
Enter an integer: 10
You entered the integer: 10

"""
"""
Enter an integer: Anchal
Error: The input is not a valid int

"""
