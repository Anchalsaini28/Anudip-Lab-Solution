# Lab 1: Write a Pandas program to create a Pivot table and find the total sale amount region wise, manager wise, sales man wise.
# Input:Download the file salesdata.csv From LMS Output:


# Importing the necessary library
import pandas as pd

# Loading the sales data from the CSV file
# Make sure to specify the correct path where 'salesdata.csv' is located
sales_data = pd.read_csv('salesdata.csv')

# Displaying the first few rows of the DataFrame to understand its structure
print("Sample data:")
print(sales_data.head())

# Creating a Pivot table to find the total sale amount
# The Pivot table is grouped by 'Region', 'Manager', and 'SalesMan'
# Aggregating the 'Sale_amt' column using sum to get the total sales
pivot_table = pd.pivot_table(sales_data, values='Sale_amt', 
                             index=['Region', 'Manager', 'SalesMan'], 
                             aggfunc='sum')

# Displaying the Pivot table
print("\nTotal sale amount region-wise, manager-wise, and sales man-wise:")
print(pivot_table)



# Output:

# Sample data:
#     Region  Manager   SalesMan          Item  Units  Unit_price  Sale_amt
# 0     East   Martha  Alexander    Television     95      1198.0  113810.0
# 1  Central  Hermann     Shelli  Home Theater     50       500.0   25000.0
# 2  Central  Hermann       Luis    Television     36      1198.0   43128.0
# 3  Central  Timothy      David    Cell Phone     27       225.0    6075.0
# 4     West  Timothy    Stephen    Television     56      1198.0   67088.0

# Total sale amount region-wise, manager-wise, and sales man-wise:
#                            Sale_amt
# Region  Manager SalesMan           
# Central Douglas John       124016.0
#         Hermann Luis       206373.0
#                 Shelli      33698.0
#                 Sigal      125037.5
#         Marth   Steven      14000.0
#         Martha  Steven     185690.0
#         Timothy David      140955.0
# East    Douglas Karen       48204.0
#         Martha  Alexander  236703.0
#                 Diana       36100.0
# West    Douglas Michael     66836.0
#         Timothy Stephen     88063.0
