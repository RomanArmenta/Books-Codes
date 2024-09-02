import numpy as np
def feature_scaling(data: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
	# Your code here
	m, n = data.shape
	standarized_data, normalized_data = np.zeros((m,n)), np.zeros((m,n))
	normalized_data = (data - np.min(data, axis=0))/(np.max(data, axis=0) - np.min(data, axis=0))
	standarized_data = (data - np.mean(data, axis=0))/(np.std(data, axis=0))
	
	return np.round(standarized_data, 4), np.round(normalized_data, 4)