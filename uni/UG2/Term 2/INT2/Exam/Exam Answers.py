# Question 1 ~ continued #2
# (vi)
import numpy as np
def margin(x, y, theta, theta_0):
    return y * ((theta.T @ x) + theta_0) / np.linalg.norm(theta)


# Question 2 ~ continued
# (iv)
import numpy as np

def top_bottom_count_feature(image):
    (rows, cols) = image.shape
    if rows != 2 and cols != 1:
        # reducing cols first
        theta_cols = np.ones((cols, 1))
        reducing_cols = image @ theta_cols
        # reducing rows now
        theta_rows = np.ones((2, rows))
        reducing_rows = theta_rows @ reducing_cols
        return reducing_rows

