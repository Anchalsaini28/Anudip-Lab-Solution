# 2. Calculate the profit made by a company

# Input: revenue = np.array([10000, 12000, 11000, 10500]) 

# expenses = np.array([4000, 5000, 4500, 4800])

# Output: Profit: [6000 7000 6500 5700]

import numpy as np

# Step 1: Define the revenue and expenses for the company using numpy arrays
revenue = np.array([10000, 12000, 11000, 10500])  # Revenue for each time period
expenses = np.array([4000, 5000, 4500, 4800])     # Expenses for each time period

# Step 2: Calculate the profit by subtracting expenses from revenue element-wise
profit = revenue - expenses  # Profit for each time period

# Output the profit
print("Profit:", profit)

# Output:-

"""
Profit: [6000 7000 6500 5700]

"""
