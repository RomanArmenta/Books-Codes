import numpy as np

def shuffle_data_mine(X, y, seed=None):
    if len(X)!=len(y):
        assert f"Cabrón"
    if seed:
        np.random.seed(seed)
    order = list(np.arange(len(y)))
    X_new = []
    y_new = []
    for i in range(len(y)):
        pick = np.random.randint(0, len(order))
        X_new.append(X[order[pick]])
        y_new.append(y[order[pick]])
        order.pop(pick)
    return np.array(X_new), np.array(y_new)

# They do the same, but with shiffle numpy array

def shuffle_data(X, y, seed=None):
    if seed:
        np.random.seed(seed)
    idx = np.arange(X.shape[0])
    np.random.shuffle(idx)
    return X[idx], y[idx]