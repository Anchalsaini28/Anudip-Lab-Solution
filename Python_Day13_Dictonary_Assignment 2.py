# 2.Write a Python script to concatenate the following dictionaries to create a new one. 

# Sample Dictionary : dic1={1:10, 2:20} dic2={3:30, 4:40} dic3={5:50,6:60} 

# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Define the sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Step 1: Create an empty dictionary to store the concatenated result
# This dictionary will hold all key-value pairs from the dictionaries being merged
concatenated_dict = {}

# Step 2: Update the concatenated dictionary with the key-value pairs from dic1
# We use the `update()` method to add the items from dic1
concatenated_dict.update(dic1)

# Step 3: Update the concatenated dictionary with the key-value pairs from dic2
# Similarly, use `update()` to add items from dic2
concatenated_dict.update(dic2)

# Step 4: Update the concatenated dictionary with the key-value pairs from dic3
# Again, use `update()` to include items from dic3
concatenated_dict.update(dic3)

# Print the result
print("The concatenated dictionary is:", concatenated_dict)

# Expected Result should be: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


# Output:-

"""
The concatenated dictionary is: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

"""
