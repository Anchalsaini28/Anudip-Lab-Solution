"""
1: Write a Pandas program to create a dataframe from a dictionary and display it.

 Sample data:

 score={'Math':[78,85,96,80,86], 'English':[84,94,89,83,86],'Hindi':[86,97,96,72,83]}
"""

# Step 1: Import the pandas library
import pandas as pd

# Step 2: Define the dictionary with sample data
score = {
    'Math': [78, 85, 96, 80, 86],      # Scores in Math
    'English': [84, 94, 89, 83, 86],   # Scores in English
    'Hindi': [86, 97, 96, 72, 83]      # Scores in Hindi
}

# Step 3: Create a DataFrame from the dictionary
# The keys of the dictionary will become the column names of the DataFrame
df = pd.DataFrame(score)

# Step 4: Display the DataFrame
print(df)

# Output
"""

   Math  English  Hindi
0    78       84     86
1    85       94     97
2    96       89     96
3    80       83     72
4    86       86     83

"""