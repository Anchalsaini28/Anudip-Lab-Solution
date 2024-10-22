# Lab2: Using SciPy Linear Algebra please solve the below problem.
# Input: 7x + 2y = 8
#        4x + 5y = 10

# Import necessary libraries
import numpy as np  # Used for numerical operations and creating matrices
from scipy import linalg  # SciPy library for solving linear algebra problems

# Define the coefficients of the equations as a matrix A
# A is a 2x2 matrix containing the coefficients of x and y in the system of equations
# Equation 1: 7x + 2y = 8 -> coefficients are [7, 2]
# Equation 2: 4x + 5y = 10 -> coefficients are [4, 5]
A = np.array([[7, 2], [4, 5]])

# Define the constants on the right-hand side as matrix B
# B is a 1x2 matrix representing the constant terms (8 and 10) on the right-hand side of the equations
B = np.array([8, 10])

# Solve the system of linear equations
# linalg.solve() finds the values of x and y by solving the matrix equation A * [x, y] = B
solution = linalg.solve(A, B)

# Extracting x and y from the solution
# The solution is an array containing the values of x and y in that order
x, y = solution

# Display the solution
# The solution is printed in a readable format, showing the values of x and y
print(f"Solution: x = {x}, y = {y}")

# Output:
# The printed solution will be:
# Solution: x = 0.7407407407407407, y = 1.4074074074074074
