# 2.Compute the standard deviation of the NumPy array

# Input: arr = [20, 2, 7, 1, 34]

# Step 1: Import the NumPy library, which provides various functions for numerical operations
import numpy as np

# Step 2: Define a NumPy array with the given input values
# In this case, we have an array with the elements 20, 2, 7, 1, and 34
arr = np.array([20, 2, 7, 1, 34])

# Step 3: Compute the standard deviation of the array
# Standard deviation is a measure of how spread out the numbers are from the mean (average)
# The formula for standard deviation is the square root of the variance.
# Variance is the average of the squared differences from the mean.
std_deviation = np.std(arr)

# Step 4: Output the computed standard deviation
# The result will show how much the numbers deviate from the mean
print("Standard Deviation of the array:", std_deviation)

# Output:-

"""
Standard Deviation of the array: 12.576167937809991

"""
