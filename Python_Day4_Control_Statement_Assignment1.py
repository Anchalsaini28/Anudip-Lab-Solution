# 1. Write a Python program that takes a number as input and prints "Even" if the number is even and "Odd" if it's odd.

# This program determines whether a given number is even or odd.

# Get the number from the user as input
number = int(input("Enter a number: "))

# Check if the number is divisible by 2 without leaving a remainder
if number % 2 == 0:
    # If the remainder is 0, the number is even
    print("Even")
else:
    # If the remainder is not 0, the number is odd
    print("Odd")
    
# Answer:- Input:- Enter a number: 8, Output:- Even
