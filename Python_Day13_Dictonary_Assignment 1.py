# 1. Write a Python program and calculate the mean of the below dictionary.

# test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4} 

# Output: 6.2

# Define the dictionary with sample data
test_dict = {"A": 6, "B": 9, "C": 5, "D": 7, "E": 4}

# Step 1: Extract the values from the dictionary
# We use the `values()` method to get a view of the dictionary's values
values = test_dict.values()

# Step 2: Calculate the sum of the values
# We use the `sum()` function to get the total of all values
total_sum = sum(values)

# Step 3: Count the number of values
# We use the `len()` function to get the count of values
count = len(values)

# Step 4: Calculate the mean
# The mean is the total sum divided by the count of values
mean = total_sum / count

# Print the result
print(f"The mean of the values in the dictionary is: {mean}")


#Output:-

"""
The mean of the values in the dictionary is: 6.2

"""
