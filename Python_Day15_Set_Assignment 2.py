# 2. Write a Python program to Return a set of elements present in Set A or B, but not both.

# Input: set1 = {10, 20, 30, 40, 50} set2 = {30, 40, 50, 60, 70} 

# Output: {20, 70, 10, 60}


# Define the two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Print the original sets for reference
print("Original Set 1:", set1)
print("Original Set 2:", set2)

# Find the symmetric difference of both sets
symmetric_diff = set1.symmetric_difference(set2)

# Print the result
print("Elements present in either set1 or set2, but not in both:", symmetric_diff)

# Output:-

"""
Original Set 1: {50, 20, 40, 10, 30}
Original Set 2: {50, 70, 40, 60, 30}
Elements present in either set1 or set2, but not in both: {20, 70, 10, 60}

"""
