# 2. Write a python program finding the factorial of a given number using a while loop

def factorial(number):
  """Calculates the factorial of a given number using a while loop.

  Args:
    number: The number whose factorial to calculate.

  Returns:
    The factorial of the given number.
  """

  if number < 0:
    return "Factorial of a negative number is undefined."

  factorial = 1
  while number > 0:
    factorial *= number
    number -= 1

  return factorial

# Get input from the user
num = int(input("Enter a number: "))

# Calculate and print the factorial
result = factorial(num)
print("Factorial of", num, "is", result)

# Answer:-

""" Enter a number: 8
Factorial of 8 is 40320 """
