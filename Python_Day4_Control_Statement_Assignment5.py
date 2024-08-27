# Write a Python program that determines the largest of three

# Prompt the user to input three numbers
# We use input() to get the user's input as strings
# We then convert each input to a float to handle both integers and decimals

# Input the first number
num1 = float(input("Enter the first number: "))

# Input the second number
num2 = float(input("Enter the second number: "))

# Input the third number
num3 = float(input("Enter the third number: "))

# We now have three numbers and need to determine which one is the largest

# Check if the first number is greater than or equal to both the second and third numbers
if num1 >= num2 and num1 >= num3:
    # If true, the first number is the largest
    print(f"The largest number is {num1}")

# Check if the second number is greater than or equal to both the first and third numbers
elif num2 >= num1 and num2 >= num3:
    # If true, the second number is the largest
    print(f"The largest number is {num2}")

# If neither the first nor the second number is the largest, the third number must be the largest
else:
    # The third number is the largest
    print(f"The largest number is {num3}")
    
# Answer:- Input:- Enter the first number: 8, Input:- Enter the second number: 7, Input:-Enter the third number: 10, Output:- The largest number is 10.0
