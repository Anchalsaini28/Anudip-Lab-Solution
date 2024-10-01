#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Step 1: Import the necessary library
import matplotlib.pyplot as plt

# Step 2: Define the days and temperature data
days = list(range(1, 32))  # Days of the month (1 to 31)
temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]  # Daily temperatures

# Step 3: Set the figure size (optional)
plt.figure(figsize=(10, 6))  # Make the chart larger

# Step 4: Create a line chart
plt.plot(days, temperature, marker='o', color='orange', linestyle='-', linewidth=2, markersize=6)

# Step 5: Add labels and title
plt.xlabel('Days of the Month')  # Label for x-axis
plt.ylabel('Temperature (°F)')   # Label for y-axis
plt.title('Daily Temperature Changes Over a Month')  # Title of the chart

# Step 6: Display the line chart
plt.grid(True)  # Add gridlines for better readability
plt.show()


# In[ ]:





# In[ ]:




