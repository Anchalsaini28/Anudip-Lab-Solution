# Write a function in python to read the content from a text file "ABC.txt" line by line and display the same on screen.

# Function to read and display content of a file line by line
def read_file():
    try:
        # Open the file in read mode
        with open("ABC.txt", "r") as file:
            # Loop through each line in the file
            for line in file:
                # Print the line (newline characters are handled automatically)
                print(line, end="")  # end="" prevents adding extra newlines

    except FileNotFoundError:
        # If the file is not found, print an error message
        print("The file 'ABC.txt' was not found.")

# Call the function to read and display the file content
read_file()


# Output:

# (File is found Output):
# Hello, This is the first line of program,
# and this is the second line of program.

# (If the File is not found Output):
# The file 'ABC.txt' was not found.

