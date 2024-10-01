#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Step 1: Import the necessary library
import matplotlib.pyplot as plt

# Step 2: Define the categories and expenses
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
expenses = [1200, 400, 200, 150, 250]  # Monthly expenses

# Step 3: Set the figure size (width, height)
plt.figure(figsize=(10, 6))  # Makes the chart bigger

# Step 4: Create a bar chart
plt.bar(categories, expenses, color='Purple')  # 'Purple' adds a soft color to the bars

# Step 5: Add labels and title
plt.xlabel('Spending Categories')  # Label for x-axis
plt.ylabel('Expenses (in USD)')    # Label for y-axis
plt.title('Monthly Expenses by Category')  # Title of the chart

# Step 6: Display the bar chart
plt.show()


# In[ ]:





# In[ ]:




