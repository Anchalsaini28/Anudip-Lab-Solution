# 1. Write a Python program to count the occurrences of each word in a given sentence.
# string = “To change the overall look of your document. To change the look available in the gallery”

# Define the sentence to analyze
sentence = "To change the overall look of your document. To change the look available in the gallery"

# Step 1: Convert the sentence to lowercase to ensure the word count is case-insensitive
sentence_lower = sentence.lower()

# Step 2: Remove punctuation from the sentence to count words accurately
# Import the string module to access punctuation characters
import string

# Create a translation table to remove punctuation
translator = str.maketrans('', '', string.punctuation)
# Remove punctuation from the sentence
sentence_no_punctuation = sentence_lower.translate(translator)

# Step 3: Split the sentence into words based on whitespace
words = sentence_no_punctuation.split()

# Step 4: Create a dictionary to store the count of each word
word_count = {}

# Step 5: Iterate over each word and update the count in the dictionary
for word in words:
    if word in word_count:
        # Increment the count of the word if it already exists in the dictionary
        word_count[word] += 1
    else:
        # Add the word to the dictionary with a count of 1 if it's not already present
        word_count[word] = 1

# Step 6: Print the word count dictionary to display the results
print("Word Count:")
for word, count in word_count.items():
    print(f"{word}: {count}")

# Answer:-

"""
Word Count:
to: 2
change: 2
the: 3
overall: 1
look: 2
of: 1
your: 1
document: 1
available: 1
in: 1
gallery: 1

"""

