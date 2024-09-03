# 2. Write a Python program to remove duplicate characters of a given string.

# Input = “String and String Function” Output: String and Function

def remove_duplicate_words(input_string):
    """
    Function to remove duplicate words from a given string.
    It retains the first occurrence of each word and removes subsequent duplicates.

    Parameters:
    input_string (str): The string from which duplicate words need to be removed.

    Returns:
    str: A string with duplicate words removed.
    """
    # Split the input string into words
    words = input_string.split()
    
    # Initialize a list to keep track of words that have been encountered
    seen_words = []
    
    # Initialize a list to store the result
    result_words = []
    
    # Iterate over each word in the list of words
    for word in words:
        # If the word has not been encountered before, add it to the result
        if word.lower() not in seen_words:
            result_words.append(word)
            seen_words.append(word.lower())  # Use lower() to ensure case-insensitivity
    
    # Join the result words back into a single string with spaces
    result_string = ' '.join(result_words)
    
    return result_string

# Example usage
input_string = "string and string function"
output_string = remove_duplicate_words(input_string)
print("Input:", input_string)
print("Output:", output_string)

# Answer:-

"""
Input: string and string function
Output: string and function

"""
