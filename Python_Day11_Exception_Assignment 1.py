# 1. Write a Python program to handle a ZeroDivisionError exception when dividing a number by zero.

def divide_numbers():
    try:
        # Prompt user for input
        numerator = float(input("Enter the numerator: "))
        denominator = float(input("Enter the denominator: "))
        
        # Perform division
        result = numerator / denominator
        
        # Display the result
        print(f"The result of the division is: {result}")
        
    except ZeroDivisionError:
        # Handle division by zero error
        print("Error: Division by zero is not allowed.")
    except ValueError:
        # Handle non-numeric input
        print("Error: Please enter numeric values only.")

# Call the function
divide_numbers()

# Answer:-

"""
Enter the numerator: 49
Enter the denominator: 7
The result of the division is: 7.0

"""
