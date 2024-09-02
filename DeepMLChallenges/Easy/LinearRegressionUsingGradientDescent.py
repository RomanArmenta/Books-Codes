import numpy as np

def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
	# Your code here, make sure to round
	m, n = X.shape
	theta = np.zeros((n, 1))
	for i in range(iterations):
		Y_pred = theta.T @ X.T
		D_m = (-1/m) * (y - Y_pred) @ X
		theta -= alpha * D_m.T
		
	return np.round(np.transpose(theta).flatten(), 4)