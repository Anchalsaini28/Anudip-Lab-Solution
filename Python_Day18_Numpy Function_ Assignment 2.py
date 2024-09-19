# 2.Suppose you have two sets of employee data—one containing information about full-time employees and another containing information about part-time employees. You want to combine this data to create a comprehensive employee dataset for HR analysis. 

"""
Input: # Employee data for full-time employees

 full_time_employees = np.array([

 [101, 'John Doe', 'Full-Time', 55000],

 [102, 'Jane Smith', 'Full-Time', 60000], 

[103, 'Mike Johnson', 'Full-Time', 52000] 

])

 # Employee data for part-time employees :

part_time_employees = np.array([ 

[201, 'Alice Brown', 'Part-Time', 25000], 

[202, 'Bob Wilson', 'Part-Time', 28000],

 [203, 'Emily Davis', 'Part-Time', 22000]

 ])
 
 """
# Importing the necessary library
import numpy as np

# Step 1: Create a numpy array with full-time employee data
full_time_employees = np.array([
    [101, 'John Doe', 'Full-Time', 55000],
    [102, 'Jane Smith', 'Full-Time', 60000],
    [103, 'Mike Johnson', 'Full-Time', 52000]
])

# Step 2: Create a numpy array with part-time employee data
part_time_employees = np.array([
    [201, 'Alice Brown', 'Part-Time', 25000],
    [202, 'Bob Wilson', 'Part-Time', 28000],
    [203, 'Emily Davis', 'Part-Time', 22000]
])

# Step 3: Concatenate the full-time and part-time employee arrays
# The concatenate function combines arrays along a specified axis.
# Axis=0 combines them row-wise (stacking one below the other).
combined_employees = np.concatenate((full_time_employees, part_time_employees), axis=0)

# Step 4: Print the combined employee dataset
print("Combined Employee Dataset for HR Analysis:")
print(combined_employees)

# Output:-

"""
Combined Employee Dataset for HR Analysis:
[['101' 'John Doe' 'Full-Time' '55000']
 ['102' 'Jane Smith' 'Full-Time' '60000']
 ['103' 'Mike Johnson' 'Full-Time' '52000']
 ['201' 'Alice Brown' 'Part-Time' '25000']
 ['202' 'Bob Wilson' 'Part-Time' '28000']
 ['203' 'Emily Davis' 'Part-Time' '22000']]

"""

