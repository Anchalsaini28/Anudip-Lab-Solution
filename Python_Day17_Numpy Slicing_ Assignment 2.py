# 2. Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.

# Step 1: Import the NumPy library
import numpy as np

# Step 2: Create an array with values ranging from 2 to 10
# We use np.arange() to generate numbers from 2 to 10.
# This will create a one-dimensional array.
array = np.arange(2, 11)  # 11 is exclusive, so the range is 2 to 10

# Step 3: Reshape the array into a 3x3 matrix
# We use the reshape() method to convert the 1D array into a 3x3 matrix.
matrix = array.reshape(3, 3)

# Step 4: Print the resulting 3x3 matrix
print("3x3 matrix with values ranging from 2 to 10:")
print(matrix)

# Output:-

"""
3x3 matrix with values ranging from 2 to 10:
[[ 2  3  4]
 [ 5  6  7]
 [ 8  9 10]]

"""
