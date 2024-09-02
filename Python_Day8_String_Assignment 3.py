# 3. Write a Python program to reverse words in a string 
# String = “Deeptech Python Training”

# Define the string with words to be reversed
input_string = "Deeptech Python Training"

# Step 1: Split the string into a list of words based on whitespace
words_list = input_string.split()

# Step 2: Reverse the order of words in the list
reversed_words_list = words_list[::-1]

# Step 3: Join the reversed list of words back into a single string with spaces in between
reversed_string = ' '.join(reversed_words_list)

# Step 4: Print the reversed string to display the result
print("Reversed Words String:")
print(reversed_string)

# Answer:-

"""
Reversed Words String:
Training Python Deeptech

"""
