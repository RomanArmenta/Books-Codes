# Exercise 1.4

# Use the Buffon's needle problem to find pi

import numpy as np
import scipy as sp

M = 1_000_000
N = 0
M_o = 0
for i in range(M):
    M_o += 1
    #center_i = 1.5*2*(0.5 - np.random.uniform())
    #x_i = min(abs(-0.5 - center_i), abs(0.5 - center_i))
    x_i = np.random.uniform()
    sin_theta_i = np.random.uniform()
    if x_i + 0.5*sin_theta_i >= 1.0 or x_i - 0.5*sin_theta_i <= 0.:
        N += 1
    else:
        continue



print(2*M/N, N)