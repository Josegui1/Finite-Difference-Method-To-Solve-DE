# Using finite difference method to solve a simple trigonometric ODE
# The equation is: du/dt = cos(t), in [0, 4pi], with the condition u0 = 0.
# Is trivial to see that the real solution is simply sin(t). 

import numpy as np
import scipy as sp
import seaborn as sns

# First step: dividing the interval, fiding h and the number of discrete points
# Supose we want to divide the domains [0, 4pi] into 1000 pieces. He have:
    
# number of pieces 
n = 2000

# the size of the step
h = (4*np.pi)/n

# Second step: finding the diference matrix for the problem
# In this problem, the derivative order is 1, so it has the recurrence relation:
# Ui+1 - Ui / h, with the condition U0 = 0. So the matrix must be 

def diff_matrix(number_of_pieces):
    
    # Creating a null matrix with the order of the discrete points
    diff_matrix = np.zeros((number_of_pieces+1, number_of_pieces+1))
    
    # Replacing the diagonal with 1's
    np.fill_diagonal(diff_matrix, 1)
    
    # Replacing the diagonal below the prinicpal diagonal with -1 
    for num in range(1, n+1):
        diff_matrix[num, num-1] = -1
    
    return diff_matrix
        
# Third step: finding b
# The right side of the equation is a n+1-dimensional vector with h * cos(ti), where ti are the points

# Creating the vector of each discrete point
x = np.linspace(0, 4*np.pi, n+1)

# Creating the right side of the equation
b = h * np.cos(x)
b = np.delete(b, -1)
b = np.insert(b, 0, 0)

# Fourth step: solving for u and plotting the solutions.

d = diff_matrix(n)

# Aproximate solution
u = sp.linalg.solve(d, b)

# Real solution
x_real = np.linspace(0, 4*np.pi, 10000)
y = np.sin(x_real)

# Graphics
real_solution = sns.lineplot(x = x_real, y = y, color="red").set_title(f"n = {n} aproximation")
aproximate_solution = sns.lineplot(x = x, y = u, color="black")



