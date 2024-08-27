# 3. Write a Python program that determines if a given year is a leap year or not.

# This program determines whether a given year is a leap year or not.

# Define a function to check if a year is a leap year

def is_leap_year(year):
    # Check if the year is divisible by 4
    if year % 4 == 0:
        # If the year is divisible by 100, it might not be a leap year
        if year % 100 == 0:
            # If the year is also divisible by 400, it is a leap year
            if year % 400 == 0:
                return True  # Leap year
            else:
                return False  # Not a leap year
        else:
            return True  # Leap year (divisible by 4, but not by 100)
    else:
        return False  # Not a leap year (not divisible by 4)

# Input: User provides a year to check
year = int(input("Enter a year: "))

# Check if the year is a leap year using the function
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Answer:- Input:- Enter a year: 2024, Output:- 2024 is a leap year.
