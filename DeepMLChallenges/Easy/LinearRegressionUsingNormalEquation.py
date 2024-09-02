import numpy as np

def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
	n_ren, n_col = len(a), len(a[0])
	b = [[0 for i in range(n_ren)] for j in range(n_col)]
	for i in range(n_col):
		for j in range(n_ren):
			b[i][j] = a[j][i]
	return b

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
	X_T = transpose_matrix(X)
	ft = np.linalg.inv(np.dot(X_T, X))
	st = np.dot(X_T, y)
	theta = np.dot(ft, st)
	
	return theta