# 1. Write a NumPy program to create an array of 10 zeros, 10 ones, and 10 fives.

# Importing the NumPy library
# NumPy is a fundamental package for numerical computations in Python
import numpy as np

# Step 1: Create an array of 10 zeros
# The np.zeros() function generates an array filled with zeros
zeros_array = np.zeros(10)
print("Array of 10 zeros:", zeros_array)

# Step 2: Create an array of 10 ones
# The np.ones() function generates an array filled with ones
ones_array = np.ones(10)
print("Array of 10 ones:", ones_array)

# Step 3: Create an array of 10 fives
# We can create an array of fives by first creating an array of ones and then multiplying it by 5
fives_array = np.ones(10) * 5
print("Array of 10 fives:", fives_array)

# Output:

"""
Array of 10 zeros: [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
Array of 10 ones: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
Array of 10 fives: [5. 5. 5. 5. 5. 5. 5. 5. 5. 5.]

"""
