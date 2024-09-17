# 1. Convert the below list into numpy array then display the array
# Input: my_list = [1, 2, 3, 4, 5] 

# Step 1: Import the NumPy library
# NumPy is a library used for working with arrays and performing numerical operations
import numpy as np

# Step 2: Define the list
# Here we create a simple Python list with some integer values
my_list = [1, 2, 3, 4, 5]

# Step 3: Convert the list to a NumPy array
# The function np.array() is used to convert a Python list into a NumPy array
my_array = np.array(my_list)

# Step 4: Display the NumPy array
# This prints the array to the console
print("NumPy array:", my_array)

# Step 5: Check the type to ensure it's a NumPy array
# We use type() to confirm that the data structure is a NumPy array
print("Type of my_array:", type(my_array))

# Output:-

"""
NumPy array: [1 2 3 4 5]
Type of my_array: <class 'numpy.ndarray'>

"""
