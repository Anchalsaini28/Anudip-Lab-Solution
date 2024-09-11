# 3.Write a Python program to find duplicate values from a list and display those

# Step 1: Define a function that finds duplicate values in a list
def find_duplicates(input_list):
    # Step 2: Initialize an empty list to store duplicate values
    duplicates = []

    # Step 3: Initialize an empty set to keep track of seen values
    seen = set()

    # Step 4: Iterate through each item in the input list
    for item in input_list:
        # Step 5: Check if the item is already in the seen set
        if item in seen:
            # Step 6: If the item is already in duplicates list, skip it to avoid adding it multiple times
            if item not in duplicates:
                # Step 7: Add the item to the duplicates list if not already added
                duplicates.append(item)
        else:
            # Step 8: Add the item to the seen set to mark it as encountered
            seen.add(item)

    # Step 9: Return the list of duplicate values
    return duplicates


# Step 10: Define a list with some duplicate values
input_list = [1, 2, 3, 4, 5, 3, 6, 7, 2, 8, 9, 1]

# Step 11: Call the function with the input list and store the result
duplicate_values = find_duplicates(input_list)

# Step 12: Display the duplicate values
print("Duplicate values in the list are:", duplicate_values)

# Output:-

"""
Duplicate values in the list are: [3, 2, 1]

"""
