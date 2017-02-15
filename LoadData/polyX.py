import numpy as np


def polyX(X):
    X = np.column_stack((X, np.log(X[:, 0])))
    X = np.column_stack((X, np.power(X[:, 0], 0.5)))
    X = np.column_stack((X, np.power(X[:, 0], 2)))
    # X = np.column_stack((X, np.power(X[:, 0], 3)))
    # X = np.column_stack((X, np.power(X[:, 0], 4)))
    # X = np.column_stack((X, np.power(X[:, 0], 5)))
    X = np.column_stack((np.array(np.ones(X.shape[0])).T, X))
    return X
