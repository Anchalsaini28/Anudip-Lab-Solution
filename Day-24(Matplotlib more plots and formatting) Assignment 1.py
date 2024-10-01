#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Step 1: Import the necessary library
import matplotlib.pyplot as plt

# Step 2: Define the income sources and monthly income data
income_sources = ['Salary', 'Freelance', 'Investments', 'Rental', 'Other']
monthly_income = [5000, 1500, 1000, 600, 400]  # Monthly income distribution

# Step 3: Set the figure size (optional)
plt.figure(figsize=(8, 8))  # Making the chart size bigger

# Step 4: Create a pie chart
plt.pie(monthly_income, labels=income_sources, autopct='%1.1f%%', startangle=90, colors=['skyblue', 'lightgreen', 'orange', 'pink', 'lightcoral'])

# Step 5: Add a title
plt.title('Monthly Income Distribution by Source')

# Step 6: Display the pie chart
plt.show()


# In[ ]:




