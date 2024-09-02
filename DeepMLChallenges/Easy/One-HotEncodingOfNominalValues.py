import numpy as np

def to_categorical(x, n_col=None):
	# Your code here
	if n_col == None or n_col < int(np.max(x)) + 1:
		n_col = int(np.max(x)) + 1
	
	
	x_oh = []
	
	for i in range(len(x)):
		x_oh.append([0. for m in range(n_col)])
		x_oh[i][x[i]] = 1.
	return x_oh