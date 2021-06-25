import numpy as np

def signed_dist(p, theta, theta_0):
    """
    Computes the signed perpendicular distance from the point p to the hyperplane defined by theta and theta_0.
    Extends numpy functions. Implements no costly loops of its own.
    :param p: column vector of size (d x 1) input. Alternatively (technically) a data point.
    :param theta: The weight, is a component that defines the linear classifier/hyperplane.
    :param theta_0: The bias, is a component that defines the linear classifier/hyperplane.
    :return: The perpendicular distance between where this vector ends and the
    hyperplane, is what is returned.
    """
    return (np.matmul(p.T, theta) + theta_0) / np.linalg.norm(theta)  # the denominator is the magnitude of theta

point = np.array([4, -1/2])
theta_normal = np.array([3, 4])
theta_zero = 5

# in debug mode:
# signed_dist(point, theta_normal, theta_zero)  # returns 3.0 as expected
