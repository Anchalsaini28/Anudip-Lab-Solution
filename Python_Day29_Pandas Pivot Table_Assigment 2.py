# Lab 2: Write a Pandas program to create a Pivot table and find the item wise unit sold.
# Input:Download the file salesdata.csv From LMS


# Importing the necessary library
import pandas as pd

# Loading the sales data from the CSV file
# Make sure to specify the correct path where 'salesdata.csv' is located
sales_data = pd.read_csv('salesdata.csv')

# Displaying the first few rows of the DataFrame to understand its structure
print("Sample data:")
print(sales_data.head())

# Creating a Pivot table to find the item-wise units sold
# The Pivot table is grouped by 'Item' and sums the 'Units' column to get the total units sold for each item
pivot_table = pd.pivot_table(sales_data, values='Units', 
                             index=['Item'], 
                             aggfunc='sum')

# Displaying the Pivot table
print("\nItem-wise total units sold:")
print(pivot_table)



# Output:

# Sample data:
#     Region  Manager   SalesMan          Item  Units  Unit_price  Sale_amt
# 0     East   Martha  Alexander    Television     95      1198.0  113810.0
# 1  Central  Hermann     Shelli  Home Theater     50       500.0   25000.0
# 2  Central  Hermann       Luis    Television     36      1198.0   43128.0
# 3  Central  Timothy      David    Cell Phone     27       225.0    6075.0
# 4     West  Timothy    Stephen    Television     56      1198.0   67088.0

# Item-wise total units sold:
#               Units
# Item               
# Cell Phone      278
# Desk             10
# Home Theater    722
# Television      716
# Video Games     395
