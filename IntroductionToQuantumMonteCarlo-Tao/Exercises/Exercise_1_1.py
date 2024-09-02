#Exercise 1.1

# Appli the Monte Carlo quadrature to evaluaate integral 
# x^2 exp(-(x^2 + y^2)) from 0 to 1 in x and y.

import numpy as np
import scipy as sp

# First, define the function
def function(x, y):
    return (x**2)*np.exp(-1*(x**2 + y**2))

# Define the number of points to take in Monte Carlo 
# simulation
M = 1_000_000

# Initial value of the integral
S = 0

# Standard deviation
ds = 0

for i in range(M):
    x_i = np.random.uniform()
    y_i = np.random.uniform()

    S += function(x_i, y_i)
    ds += function(x_i, y_i)**2

S /= M
ds /= M
ds = np.sqrt(np.abs(ds - S**2)/M)

scipy_integral = sp.integrate.dblquad(function, 0, 1, lambda x: 0, lambda x: 1)

print(f"Using M = {M}, the result of the integral is {S} with a Standard Deviation of {ds}.")
print(f"In scipy, the result is {scipy_integral[0]} with error {scipy_integral[1]}.")