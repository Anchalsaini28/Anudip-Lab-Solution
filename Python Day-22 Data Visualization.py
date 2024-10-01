#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Step 1: Import the necessary library
import matplotlib.pyplot as plt

# Step 2: Prepare the data
x = [0, 5, 9, 10, 15, 20, 25]  # x values (independent variable)
y = [0, 1, 2, 3, 4, 5, 6]      # y values (dependent variable)

# Step 3: Create the line plot with markers
# Adding 'o' as the marker symbol to display circles at each data point
plt.plot(x, y, marker='o')

# Step 4: Add labels to the axes
plt.xlabel('X-axis (Time)')      # Label for the x-axis
plt.ylabel('Y-axis (Value)')     # Label for the y-axis

# Step 5: Add a title to the plot
plt.title('Line Plot')

# Step 6: Display the plot
plt.show()


# In[ ]:




