# 4. Create a Python program that checks if a user-given number is positive, negative, or zero.

# Prompt the user to input a number
# We use input() to get the user's input as a string
# We then convert it to a float to handle both integers and decimals
number = float(input("Enter a number: "))

# Check if the number is greater than zero
if number > 0:
    # If the condition is true, the number is positive
    print(f"The number {number} is positive.")

# Check if the number is less than zero
elif number < 0:
    # If the condition is true, the number is negative
    print(f"The number {number} is negative.")

# If the number is neither greater than zero nor less than zero, it must be zero
else:
    # The number is exactly zero
    print(f"The number {number} is zero.")

# Answer:- Input:- Enter a number: 10, Output:- The number 10.0 is positive.
