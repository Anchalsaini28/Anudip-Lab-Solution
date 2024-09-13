# 1. Write a Python program to Get Only unique items from two sets.

# Define the two sets
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# Print the original sets for reference
print("Original Set 1:", set1)
print("Original Set 2:", set2)

# Find the union of both sets to get all unique items
unique_items = set1.union(set2)

# Print the result
print("Unique items from both sets:", unique_items)

# Output:-

"""
Original Set 1: {50, 20, 40, 10, 30}
Original Set 2: {50, 70, 40, 60, 30}
Unique items from both sets: {70, 40, 10, 50, 20, 60, 30}

"""
