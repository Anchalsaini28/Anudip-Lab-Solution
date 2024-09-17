# 2. Convert the below list into a numpy array then display the array then display the first and last index and then multiply each element by 2 and display the result.

# Input: my_list = [1, 2, 3, 4, 5]

# Step 1: Import the NumPy library
# NumPy provides support for arrays and numerical operations.
import numpy as np

# Step 2: Define the list
# This is a simple Python list of integers.
my_list = [1, 2, 3, 4, 5]

# Step 3: Convert the list to a NumPy array
# The np.array() function is used to convert the list into a NumPy array.
my_array = np.array(my_list)

# Step 4: Display the NumPy array
# This will print the NumPy array to the console.
print("NumPy array:", my_array)

# Step 5: Display the first index element (index 0)
# Accessing the first element of the array using index 0.
first_element = my_array[0]
print("First element:", first_element)

# Step 6: Display the last index element (index -1)
# Accessing the last element of the array using index -1 (negative index in Python).
last_element = my_array[-1]
print("Last element:", last_element)

# Step 7: Multiply each element by 2
# This performs element-wise multiplication of the array by 2.
multiplied_array = my_array * 2

# Step 8: Display the result of multiplication
# Printing the modified array where each element has been multiplied by 2.
print("Array after multiplying by 2:", multiplied_array)

# Output:-

"""
NumPy array: [1 2 3 4 5]
First element: 1
Last element: 5
Array after multiplying by 2: [ 2  4  6  8 10]

"""
