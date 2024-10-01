#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Step 1: Import the pandas library
import pandas as pd

# Step 2: Define the expense categories
categories = ['Groceries', 'Utilities', 'Rent', 'Transportation', 'Entertainment']

# Step 3: Define the monthly expense data for each category
expenses = [500, 200, 1200, 300, 150]

# Step 4: Create a Pandas Series with the categories as the index and the expenses as the values
expenses_series = pd.Series(data=expenses, index=categories)

# Step 5: Display the Pandas Series
print("Household Expenses for the Month:")
print(expenses_series)

# Step 6: Calculate the total monthly expenses
total_expenses = expenses_series.sum()
print(f"\nTotal Monthly Expenses: ${total_expenses}")

# Step 7: Find the category with the highest expense
highest_expense = expenses_series.max()
highest_category = expenses_series.idxmax()
print(f"Highest Expense: {highest_category} (${highest_expense})")

# Step 8: Find the category with the lowest expense
lowest_expense = expenses_series.min()
lowest_category = expenses_series.idxmin()
print(f"Lowest Expense: {lowest_category} (${lowest_expense})")

# Step 9: Calculate the average monthly expense
average_expense = expenses_series.mean()
print(f"Average Monthly Expense: ${average_expense:.2f}")

# Step 10: Get a summary of the expenses (basic statistics)
expense_summary = expenses_series.describe()
print(f"\nSummary Statistics:\n{expense_summary}")


# In[ ]:




