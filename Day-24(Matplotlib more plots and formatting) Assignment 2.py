#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Step 1: Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Step 2: Define the sales data
months = np.arange(1, 13)  # Months from 1 to 12
electronics_sales = np.array([25000, 28000, 31000, 27000, 30000, 32000, 35000, 36000, 38000, 39000, 41000, 42000])
clothing_sales = np.array([15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000])
home_garden_sales = np.array([18000, 19000, 20000, 21000, 22000, 23000, 24000, 25000, 26000, 27000, 28000, 29000])
sports_outdoors_sales = np.array([12000, 13000, 14000, 15000, 16000, 17000, 18000, 19000, 20000, 21000, 22000, 23000])

# Step 3: Create a figure with subplots (2 rows, 2 columns)
fig, axs = plt.subplots(2, 2, figsize=(12, 8))  # Create a 2x2 grid of subplots

# Step 4: Plot Electronics sales data in the first subplot
axs[0, 0].plot(months, electronics_sales, marker='o', color='blue', linestyle='-', linewidth=2, label='Electronics')
axs[0, 0].set_title('Electronics Sales')  # Title for the first subplot
axs[0, 0].set_xlabel('Months')  # X-axis label
axs[0, 0].set_ylabel('Sales (in USD)')  # Y-axis label
axs[0, 0].legend(loc='upper left')  # Add legend to the first subplot
axs[0, 0].grid(True)  # Add grid to the first subplot

# Step 5: Plot Clothing sales data in the second subplot
axs[0, 1].plot(months, clothing_sales, marker='o', color='green', linestyle='-', linewidth=2, label='Clothing')
axs[0, 1].set_title('Clothing Sales')  # Title for the second subplot
axs[0, 1].set_xlabel('Months')  # X-axis label
axs[0, 1].set_ylabel('Sales (in USD)')  # Y-axis label
axs[0, 1].legend(loc='upper left')  # Add legend to the second subplot
axs[0, 1].grid(True)  # Add grid to the second subplot

# Step 6: Plot Home & Garden sales data in the third subplot
axs[1, 0].plot(months, home_garden_sales, marker='o', color='orange', linestyle='-', linewidth=2, label='Home & Garden')
axs[1, 0].set_title('Home & Garden Sales')  # Title for the third subplot
axs[1, 0].set_xlabel('Months')  # X-axis label
axs[1, 0].set_ylabel('Sales (in USD)')  # Y-axis label
axs[1, 0].legend(loc='upper left')  # Add legend to the third subplot
axs[1, 0].grid(True)  # Add grid to the third subplot

# Step 7: Plot Sports & Outdoors sales data in the fourth subplot
axs[1, 1].plot(months, sports_outdoors_sales, marker='o', color='red', linestyle='-', linewidth=2, label='Sports & Outdoors')
axs[1, 1].set_title('Sports & Outdoors Sales')  # Title for the fourth subplot
axs[1, 1].set_xlabel('Months')  # X-axis label
axs[1, 1].set_ylabel('Sales (in USD)')  # Y-axis label
axs[1, 1].legend(loc='upper left')  # Add legend to the fourth subplot
axs[1, 1].grid(True)  # Add grid to the fourth subplot

# Step 8: Adjust layout to avoid overlap and display the plots
plt.tight_layout()  # Adjusts layout to prevent overlap of subplots
plt.show()  # Display the figure


# In[ ]:




