# Lab2: Write a python program using Interpolation to fill in missing values in the data frame. After that store the data frame into a MATLAB file using SciPy IO.Then display the contents from the MATLAB file. 
# Input: df = pd.DataFrame({"Math":[12, 4, 7, None, 2], "English":[4, 3, 57, 3, None], "Hindi":[20, 16, None, 3, 8], "Science":[14, 3, None, None, 6]})


# Import necessary libraries
import pandas as pd
from scipy.io import savemat, loadmat

# Step 1: Creating a DataFrame with missing values
df = pd.DataFrame({
    "Math": [12, 4, 7, None, 2],
    "English": [4, 3, 57, 3, None],
    "Hindi": [20, 16, None, 3, 8],
    "Science": [14, 3, None, None, 6]
})

# Step 2: Displaying the original DataFrame with missing values
print("Original DataFrame with missing values:")
print(df)

# Step 3: Using interpolation to fill in the missing values
df_interpolated = df.interpolate(method='linear')

# Step 4: Displaying the DataFrame after interpolation
print("\nDataFrame after applying interpolation:")
print(df_interpolated)

# Step 5: Converting the DataFrame into a dictionary for MATLAB storage
data_dict = {col: df_interpolated[col].values for col in df_interpolated.columns}

# Step 6: Storing the DataFrame into a MATLAB file using savemat
savemat("interpolated_data.mat", data_dict)

# Step 7: Loading the MATLAB file to display the contents
loaded_data = loadmat("interpolated_data.mat")

# Step 8: Displaying the contents from the MATLAB file
print("\nContents loaded from MATLAB file:")
for key, value in loaded_data.items():
    if not key.startswith("__"):
        print(f"{key}: {value}")


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

# Contents loaded from MATLAB file:
# Math: [[12.   4.   7.   4.5  2. ]]
# English: [[ 4.  3. 57.  3.  3.]]
# Hindi: [[20.  16.   9.5  3.   8. ]]
# Science: [[14.  3.  4.  5.  6.]]

