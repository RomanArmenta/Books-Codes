# Exercise 1.3

# Calculate pi by approximate by throwing darts in a cube in [0,1], 
# given that the chance to land inside the unit sphere centered at the origin is 
# pi/6

import numpy as np
import scipy as sp

# Number of darts
M = 1_000_000 * 3

# Number of darts that land on the unit sphere centered at origin
N = 0

for i in range(M):
    x_i, y_i, z_i = np.random.uniform(size = (3,))
    r = x_i**2 + y_i**2 + z_i**2
    if r<=1:
        N += 1

pi_approx = (N/M)*6

print(f"The approximation of pi by Monte Carlo is {pi_approx}.")