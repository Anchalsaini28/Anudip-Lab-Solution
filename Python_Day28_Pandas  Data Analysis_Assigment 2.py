#Q2. Write a Pandas program to split the following dataframe by school code and get mean, min, and max value of age for each school. Also generate a horizontal bar chart based on the result and explain the conclusion.
#    Input: student_data = pd.DataFrame({ 'school_code': ['s001','s002','s003','s001','s002','s004'],
#    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'], 
#    'name': ['Alberto Franco','Gino Mcneill','Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'], 
#    'age': [12, 12, 13, 13, 14, 12], 
#    'height': [173, 192, 186, 167, 151, 159], 
#    'weight': [35, 32, 33, 30, 31, 32], 
#    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']}, )

# Import the necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Create the DataFrame with the provided data
student_data = pd.DataFrame({
    'school_code': ['s001', 's002', 's003', 's001', 's002', 's004'],
    'class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    'age': [12, 12, 13, 13, 14, 12],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [35, 32, 33, 30, 31, 32],
    'address': ['street1', 'street2', 'street3', 'street1', 'street2', 'street4']
})

# Group the data by 'school_code' and calculate mean, min, and max age for each school
age_stats = student_data.groupby('school_code')['age'].agg(['mean', 'min', 'max'])

# Print the age statistics for each school
print("Age statistics for each school:\n", age_stats)

# Plot the results as a horizontal bar chart
age_stats.plot(kind='barh')

# Add title and labels to the plot
plt.title("Age Statistics by School Code")
plt.xlabel("Age")
plt.ylabel("School Code")

# Display the plot
plt.show()

# Conclusion: The horizontal bar chart shows the average, minimum, and maximum ages of students for each school.
# This information can help identify age distributions and variations within different schools.

#ANS=> Age statistics for each school:
#ANS=>               mean  min  max
#ANS=> school_code                 
#ANS=> s001         12.5   12   13 
#ANS=> s002         13.0   12   14 
#ANS=> s003         13.0   13   13 
#ANS=> s004         12.0   12   12 