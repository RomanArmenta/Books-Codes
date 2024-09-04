import numpy as np



def batch_iterator(X, y=None, batch_size=64):
	
	# Your code here 
    n_batches = int(len(X)/batch_size) + 1
    batching = []       
    if y is None:
        for i in range(n_batches):
            batching.append(X[i*batch_size: min((i+1)*batch_size, len(X))].tolist())
        return batching
    else:
        for i in range(n_batches):
            batching.append([X[i*batch_size: min((i+1)*batch_size, len(X))].tolist(), y[i*batch_size: min((i+1)*batch_size, len(X))].tolist()])
        return batching
