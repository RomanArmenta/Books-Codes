import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
	# Your code here
	m = len(y_true)
	OLS = ((1/(m))*np.dot(y_true - np.dot(X, w), y_true - np.dot(X, w)))
	regularization = (alpha*np.dot(w, w))
	return round(OLS + regularization, 3)
	
