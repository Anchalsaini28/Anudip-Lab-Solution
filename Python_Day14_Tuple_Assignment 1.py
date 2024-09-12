# 1. Write a Python program to find the number of times 4 appears in the tuple. 

# Input: tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7 ) Output: 3

# Step 1: Define the tuple with the given elements
tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7)

# Step 2: Use the count() method to find the occurrences of the number 4 in the tuple
# The count() method returns the number of times the specified element appears in the tuple
count_of_fours = tuplex.count(4)

# Step 3: Print the result with a message
# This will display the number of times 4 appears in the tuple
print("The number 4 appears", count_of_fours, "times in the tuple.")

# Output:-

"""
The number 4 appears 3 times in the tuple.

"""
