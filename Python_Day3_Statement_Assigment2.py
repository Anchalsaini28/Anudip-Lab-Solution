Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 2. Using input function take two number and then swap the number.
>>> # Take two numbers as input from the user
>>> number1 = input("Enter the first number: ")
Enter the first number: 2
>>> number2 = input("Enter the second number: ")
Enter the second number: 8
>>> # Print the original values
>>> print(f"Before swapping: number1 = {number1}, number2 = {number2}")
Before swapping: number1 = 2, number2 = 8
>>> # Swap the numbers
>>> number1, number2 = number2, number1
>>> # Print the swapped values
>>> print(f"After swapping: number1 = {number1}, number2 = {number2}")
After swapping: number1 = 8, number2 = 2
>>> # Answer:- Before swapping: number1 = 2, number2 = 8, After swapping: number1 = 8, number2 = 2
