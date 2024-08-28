# 3. Using max() and min() functions display the maximum and minimum of 5 random numbers.

# Step 1: Import the 'random' module to generate random numbers
import random

# Step 2: Generate 5 random numbers and store them in a list called 'numbers'
# Using random.randint() to generate random integers between 1 and 100
numbers = [random.randint(1, 100) for _ in range(5)]

# Step 3: Display the generated random numbers
print("The 5 random numbers are:", numbers)

# Step 4: Use the max() function to find the maximum number in the list
max_number = max(numbers)

# Step 5: Use the min() function to find the minimum number in the list
min_number = min(numbers)

# Step 6: Display the maximum and minimum numbers
print("The maximum number is:", max_number)
print("The minimum number is:", min_number)

# Answer:-
"""The 5 random numbers are: [19, 73, 92, 68, 61]
The maximum number is: 92
The minimum number is: 19 """ 
