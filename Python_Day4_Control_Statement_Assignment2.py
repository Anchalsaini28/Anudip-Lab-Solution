# 2. Create a Python program that checks whether a person is eligible to vote (18 years or older) based on their age.

# This program determines whether a person is eligible to vote based on their age.

# Get the person's age as input
age = int(input("Enter your age: "))

# Check if the age is greater than or equal to 18
if age >= 18:
    # If the age is 18 or older, the person is eligible to vote
    print("You are eligible to vote!")
else:
    # If the age is less than 18, the person is not eligible to vote
    print("You are not eligible to vote yet.")
    
# Answer:- Input:- Enter your age: 24, Output:- You are eligible to vote!
