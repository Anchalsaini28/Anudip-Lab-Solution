# Lab1: Write a python program using pandas Interpolation to fill in missing values in the data frame.
# Input: df = pd.DataFrame({"Math":[12, 4, 7, None, 2], "English":[4, 3, 57, 3, None], "Hindi":[20, 16, None, 3, 8], "Science":[14, 3, None, None, 6]})


# Import the necessary library
import pandas as pd

# Creating a DataFrame with missing values
df = pd.DataFrame({
    "Math": [12, 4, 7, None, 2],
    "English": [4, 3, 57, 3, None],
    "Hindi": [20, 16, None, 3, 8],
    "Science": [14, 3, None, None, 6]
})

# Display the original DataFrame
print("Original DataFrame with missing values:")
print(df)

# Using interpolation to fill in the missing values
# The 'method' parameter in interpolate can specify different kinds of interpolation
df_interpolated = df.interpolate(method='linear')

# Display the DataFrame after interpolation
print("\nDataFrame after applying interpolation:")
print(df_interpolated)


# Output:

# Original DataFrame with missing values:
#    Math  English  Hindi  Science
# 0  12.0      4.0   20.0     14.0
# 1   4.0      3.0   16.0      3.0
# 2   7.0     57.0    NaN      NaN
# 3   NaN      3.0    3.0      NaN
# 4   2.0      NaN    8.0      6.0

# DataFrame after applying interpolation:
#    Math  English  Hindi  Science
# 0  12.0      4.0   20.0     14.0
# 1   4.0      3.0   16.0      3.0
# 2   7.0     57.0    9.5      4.0
# 3   4.5      3.0    3.0      5.0
# 4   2.0      3.0    8.0      6.0
