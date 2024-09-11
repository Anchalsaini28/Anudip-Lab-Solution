# Write a function in Python to count and display the total number of words in a text file “ABC.txt”

# Function to count and display the total number of words in the file "ABC.txt"
def count_words():
    try:
        # Open the file in read mode
        with open("ABC.txt", "r") as file:
            # Initialize a variable to store the total word count
            word_count = 0
            
            # Loop through each line in the file
            for line in file:
                # Split the line into words using the split() method
                words = line.split()
                # Add the number of words in the current line to the total word count
                word_count += len(words)
        
        # Display the total word count
        print(f"Total number of words: {word_count}")

    except FileNotFoundError:
        # If the file is not found, print an error message
        print("The file 'ABC.txt' was not found.")

# Call the function to count and display the number of words in the file
count_words()


# Output:

# (File is found Output):
# Total number of words: 16

# (If the File is not found Output):
# The file 'ABC.txt' was not found.
