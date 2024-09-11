# 1. Write a Python program to sum all the items in a list.

# Step 1: Define a function that takes a list as an input
def sum_of_list(items):
    # Step 2: Initialize a variable to store the sum, starting at 0
    total = 0

    # Step 3: Iterate through each item in the list
    for item in items:
        # Step 4: Add each item to the total sum
        total += item

    # Step 5: Return the total sum of the list
    return total


# Step 6: Define a list of numbers
numbers = [7, 4, 3, 5, 9]

# Step 7: Call the function with the list and store the result
result = sum_of_list(numbers)

# Step 8: Print the result
print("The sum of the list is:", result)

# Output:-

"""
The sum of the list is: 28

"""
