# Exercise 1.2

# Evaluate the integral (xy + yz)r^2 e^{-r^2} in the entire three 
# dimensional space.

import numpy as np
import scipy as sp

# Define the function
def function(x, y, z):
    r = x**2 + y**2 + z**2
    return (x*y + y*z)*(r)*np.exp(-r)

# Number of triadas (x_i, y_i, z_i) to sample.
# Since there is 3 dimensions, we need more.
M = 1_000_000 * 3

# Limit of the box in where we are going to integrate.
lim = 500

S = 0
ds = 0

for i in range(M):
    x_i, y_i, z_i = 2*lim*(0.5 - np.random.uniform(size=(3,)))
    f = function(x_i, y_i, z_i)
    S += f
    ds += f*f

S /= M
ds /= M
ds = np.sqrt(np.abs(ds - S**2)/M)

sp_int = sp.integrate.nquad(function, [[-lim, lim], [-lim, lim], [-lim, lim]])

print(f"The integral by Monte Carlo with {M} samples in a box of length {lim*2} is {S} with sd of {ds}.")
print(f"The integral in the same box with scipy gives {sp_int[0]} with error of {sp_int[1]}.")