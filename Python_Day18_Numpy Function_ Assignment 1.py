# 1. Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions. Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day). 

# Input: temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2,-4,-12]) 

# Step 1: Import the numpy library for array manipulation
import numpy as np

# Step 2: Create a numpy array with temperature readings
# Each element in the array represents the temperature on a particular day
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2, -4, -12])

# Step 3: Identify the indices of hot days
# A hot day is defined as a day where the temperature is greater than 35°C
# np.where() returns the indices where the condition (temperatures > 35) is True
hot_days_indices = np.where(temperatures > 35)[0]

# Step 4: Identify the indices of cold days
# A cold day is defined as a day where the temperature is less than 5°C
# np.where() returns the indices where the condition (temperatures < 5) is True
cold_days_indices = np.where(temperatures < 5)[0]

# Step 5: Display the hot days and their corresponding temperatures
print("Hot days:")
print("Day   Temperature (°C)")
# Loop through the indices of hot days
for i in hot_days_indices:
    # i+1 is used because array indices start from 0, but we want to display days starting from 1
    # temperatures[i] gives the temperature of the corresponding hot day
    # .1f formats the temperature to one decimal place
    print(f"{i+1}     {temperatures[i]:.1f}")

# Step 6: Display the cold days and their corresponding temperatures
print("\nCold days:")  # \n adds a new line to separate the output from hot days
print("Day   Temperature (°C)")
# Loop through the indices of cold days
for i in cold_days_indices:
    # Similarly, i+1 is used to match day numbers (starting from 1)
    print(f"{i+1}     {temperatures[i]:.1f}")

# Output:-

"""
Hot days:
Day   Temperature (°C)
3     36.8
6     38.7
10     37.2

Cold days:
Day   Temperature (°C)
11     -4.0
12     -12.0

"""
