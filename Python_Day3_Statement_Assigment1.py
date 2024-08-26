Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # 1. Using input() function take one number from the user and using ternary operators check whether the number is even or odd
>>> # Take a number as input from the user
>>> number = int(input("Enter a number: "))
Enter a number: 1
>>> # Use a ternary operator to check if the number is even or odd
>>> result = "Even" if number % 2 == 0 else "Odd"
>>> # Print the result
>>> print(f"The number is {result}.")
The number is Odd.
>>> # Answer:- The number is Odd.
