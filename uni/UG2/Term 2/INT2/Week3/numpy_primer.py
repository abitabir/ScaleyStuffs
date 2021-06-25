import numpy as np

# being consistent with leccies thus far
x = np.array([1, 2, 3])  # dfining x as a (column) vector
theta = np.array([4, 5, 6])
theta_0 = 7
# np.zeros(5)  # creates numpy array of length 5, filled with zeroes
# np.zeros([5, 2])  # creates numpy array of zeroes, representing matrix of dimensions (5 x 2) ~ number of rows x number of columns
# this does the same as well: np.zeroes((5, 2))
x.shape  # gives (3,) #  numpy arrays are weird in that they do not specify whether the array is representing a (standard/column) vector or a row vector

# to create a matrix with (2 x 3) dimensions explicitly
A = np.array([[1, 2, 3], [4, 5, 6]])

# getting dot product of vector x and matrix A
dot_product_theta_and_x = np.dot(theta, x)  # errneously, cuz numpy unhelpfully doesn't distinguish between row and column vectors,
# np.dot(theta.T, x) {where .T returns the transpose of the matrix self ig} gives the same result as the line above, even though mathematically it should not

# numpy has the convention that the dot product {calculated from vectors - one column and the other row} is generalised to matrix multiplication at higher dimensions



# * does scalar multiplication, not matrix multiplication
# theta * x just actually timeses thetai with xi, doin an element devised/scalar multiplication
multiplyings = x @ theta  # should have thrown an error cuz both stored as same vector dimensions, so inner dimensions would not match,
# so attempting a matrix multiplication would be invalid, HOWEVER, numpy just sigh automatically assumes one is a column vector and the other is a row vector...
# quite dangerous, that, but, hey, how numpy works
# np.matul() function does the same as @

# creating a 3 x 4 matrix as a friend for A
B = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])

A @ B  # would work as inner dimensions match (2 x 3) @ (3 x 4)
# result would, in turn, be a (2 x 4) matrix ~ comprised of the outer dimensions
# https://numpy.org/doc/stable/reference/generated/numpy.dot.html
# if both A and B are 2D arrays, np.dot(A, B) is matrix multiplication, but using matmul or a @ b is preferred

# accessing elements
A[1]  # returns row vector (thataways ->) at index 1 {not that it can be distinguished from column XOS}
A[:, 1]  # returns column vector (thataways ^) at index 1
A[1, 2]  # accessing the element at the first row (after 0th row) and in the second column
A[-1]  # accessing the last row of the matrix

# programatically
norm_of_x_p = np.linalg.norm(x)
# somewhere in between
norm_of_x_m = np.sqrt(np.dot(x, x.T))  # np.sqrt(np.dot(x, x))  # same as
# analytically
norm_of_x_a = np.sqrt(x[0]**2 + x[1]**2 + x[2]**2)


# plottings
import matplotlib.pyplot as plt

# a good approach is to name your plot e.g axes - could have muliple windows opened at once!
# this is an object oriented programming mode in matplotlib
# useful when you need to manipulate the plot quite a bit
fig, axes = plt.subplots()  # creating an empty plot
axes.set_title("testing testing testing 123")
axes.xlabel("x")
axes.ylabel("y")
axes = plt.plot([0, 5], [0, 5], "g")
axes.scatter([1, 2, 3], [4, 5, 6], c="r")
# axes.show()  # if we were showing in the scientific mode, but the interactive mode is more useful


# later edit: actually, numpy does store column and row vectors if you define it as a 2D array!!!
x = np.array([[2], [3], [5]])
x.shape  # is (3, 1) i.e (3 x 1)
v = np.array([3, 0, 4])
y.shape  # is (1, 2) i.e (1 x 3)
x @ v  # valid multiplication
v @ x  # valid multiplication cuz inner dimensions also match this arrangement
# x.T @ v  # invalid multiplication because inner dimensions do not match

