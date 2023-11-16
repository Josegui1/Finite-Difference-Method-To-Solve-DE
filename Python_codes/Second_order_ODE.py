# Using finite differences method to solve a second order diferential equation
# The equation is: y'' + y + 1 = 0, in [0, 1] and y0 = 0 = yn and the real solution
# is : y = cost + [(1 - cos1)/sin1]sint - 1

import numpy as np
import scipy as sp
import seaborn as sns

# First step: dividing the iterval, finding h and initial conditions
# Number of pieces
n = 1000

# Step size
h = 1/n

# First boundary condition
i0 = 0

# Second boundary condition
i = 0

# Second step: finding the difference matrix for this problem
# The recurrence equation is Yi-1 + (h² -2)Yi + Yi+1 = -h²
# creating two parameters p and q, such as:

p = h*h
q = (p - 2)

# finding the difference matrix

def diff_matrix(number_of_pieces):
    # Creating a zero matrix and filling the diagonal with 1
    diff_matrix = np.zeros((n+1, n+1))
    np.fill_diagonal(diff_matrix, 1)

    # Adjusting other values of the matrix
    for num in range(0, n-1):
        diff_matrix[num+1, num+1] = q

    for num in range(1, n):
        diff_matrix[num, num-1] = 1

    for num in range(1, n):
        diff_matrix[num, num+1] = 1
        
    return diff_matrix
        
# Third step: creating b and x for plot later

# x
x = np.linspace(0, 1, n+1)
x_real = np.linspace(0, 1, 2500)

# b
b = np.repeat(-p, n+1)
b = np.delete(b, len(b)-1)
b = np.delete(b, 0)
b = np.insert(b, 0, i0)
b = np.insert(b, len(b), i)

# Fourth step: solving the system and plotting the real and aproximate solution for comparison
# System solution and real solution

d = diff_matrix(n)

u = sp.linalg.solve(d, b)

y = np.cos(x_real) + ((1- np.cos(1))/np.sin(1)) * np.sin(x_real) - 1

# graphics

real_solution = sns.lineplot(x = x_real, y = y).set_title(f"n = {n} aproximation")
aproximate_solution = sns.lineplot(x = x, y = u, color = "red")


