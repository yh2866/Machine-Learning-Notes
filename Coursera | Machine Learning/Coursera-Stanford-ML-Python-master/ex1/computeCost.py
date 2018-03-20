import numpy as np

def computeCost(X, y, theta):
    """
       computes the cost of using theta as the parameter for linear 
       regression to fit the data points in X and y
    """
    m = y.size
    J = 0
    h = X.dot(theta)
    J = 1.0/(2.0*m)*np.sum(np.square(h-y))

    return J


