#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Step 1: Import the pandas library
import pandas as pd

# Step 2: Create a list of student names
students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace', 'Hannah', 'Ivy', 'Jack']

# Step 3: Create a list of exam scores corresponding to each student
exam_scores = [92, 88, 76, 94, 82, 90, 85, 89, 78, 91]

# Step 4: Create a Pandas Series with the students as the index and their exam scores as the values
scores_series = pd.Series(data=exam_scores, index=students)

# Step 5: Display the Pandas Series
print("Pandas Series of Student Scores:")
print(scores_series)

# Step 6: Analyze the data - find the mean score
mean_score = scores_series.mean()
print(f"\nAverage Exam Score: {mean_score}")

# Step 7: Find the highest score
max_score = scores_series.max()
print(f"Highest Exam Score: {max_score}")

# Step 8: Find the student with the highest score
top_student = scores_series.idxmax()
print(f"Top Scoring Student: {top_student}")

# Step 9: Find the lowest score
min_score = scores_series.min()
print(f"Lowest Exam Score: {min_score}")

# Step 10: Find the student with the lowest score
lowest_student = scores_series.idxmin()
print(f"Lowest Scoring Student: {lowest_student}")

# Step 11: Get a summary of the exam scores (basic statistics)
summary_statistics = scores_series.describe()
print(f"\nSummary Statistics:\n{summary_statistics}")


# In[ ]:




