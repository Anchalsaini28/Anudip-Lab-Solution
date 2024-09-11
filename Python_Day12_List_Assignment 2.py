# 2. Write a Python program to get the largest and smallest number from a list without builtin functions.

# Step 1: Define a function that takes a list as input
def find_largest_and_smallest(numbers):
    # Step 2: Check if the list is empty; if so, return None for both values
    if not numbers:
        return None, None

    # Step 3: Initialize the largest and smallest variables with the first element of the list
    largest = numbers[0]
    smallest = numbers[0]

    # Step 4: Iterate through each number in the list
    for number in numbers:
        # Step 5: Check if the current number is greater than the current largest
        if number > largest:
            largest = number  # Update largest if the condition is true

        # Step 6: Check if the current number is smaller than the current smallest
        if number < smallest:
            smallest = number  # Update smallest if the condition is true

    # Step 7: Return the largest and smallest numbers
    return largest, smallest


# Step 8: Define a list of numbers
numbers = [3, 1, 9, -2, 7, 0, 5]

# Step 9: Call the function with the list and store the result
largest, smallest = find_largest_and_smallest(numbers)

# Step 10: Print the results
print("The largest number in the list is:", largest)
print("The smallest number in the list is:", smallest)

# Output:-

"""
The largest number in the list is: 9
The smallest number in the list is: -2

"""
