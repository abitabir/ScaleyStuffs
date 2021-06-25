import numpy as np

# putting all these into Python console individually is easier

# Week 3: Numpy
# 1.
# a)
x = np.array([[2], [3], [5]])
v = np.array([3, 0, 4])
xTv = x.T @ v  # x @ v gives same result numpy wise, even though mathematically it should give an error...
print(xTv)
vTx = v.T @ x  # don't use *, gives result transposed for some reason, inaccurate
print(vTx)

# b)
A = np.array([[4, 1, 0, 2], [2, 0, 1, 3]])
b = np.array([[3], [0], [5], [1]])

A.shape
b.shape

c = A @ b

# c)
A = np.array([[4, 1, 0, 2], [2, 0, 1, 3]])
B = np.array([[3, 2, 0], [0, 4, 2], [5, 0, 1], [1, 3, 4]])

C = np.matmul(A, B)  # same as A @ B or np.dot(A, B) only cuz both higher dimensions of matrices than vectors {both kinds}

# d)
w = np.array([[2], [4], [3], [1]])  # diligently inputting column vector form

llwll2_np = np.linalg.norm(w)
llwll2_maths = np.sqrt(30)
correct_norm = llwll2_np == llwll2_maths

# e)
u = np.array([[5], [0], [0]])
unit_normalised_u = u / np.linalg.norm(u)

# 2.
# accessing submatrix of B, consisting of elements of (second or third row) *and* second column only
B_submatrix = B[:, 1][1:3]  # or B[1:3, 1]  # in matrix notation usually row column, but numpy opposite

# don't overshadow inbuilt python functions XOS
def vectors_dot(v1, v2):  # inputs will be vectors, so defo dimension (1 x n) or (n x 1)
    flattened_v1 = v1.flatten()
    flattened_v2 = v2.flatten()
    dot_product = 0
    if len(flattened_v1) != 1 and len (flattened_v2) != 1 and len(flattened_v1) == len(flattened_v2):
        for i in range(len(flattened_v1)):
            dot_product += flattened_v1[i] * flattened_v2[i]
    else:
        raise Exception("input vectors are not of same length =(")
    return dot_product

def vectors_dot_list_comprehension_style(v1, v2):  # inputs will be vectors, so defo dimension (1 x n) or (n x 1)
    flattened_v1 = v1.flatten()
    flattened_v2 = v2.flatten()
    dot_product = 0
    if not len(flattened_v1) == len(flattened_v2):
        raise Exception("input vectors are not of same length =(")
    return sum([flattened_v1[i] * flattened_v2[i] for i in range(len(flattened_v1))])

def vectors_dot_zip_style(v1, v2):  # inputs will be vectors, so defo dimension (1 x n) or (n x 1)
    flattened_v1 = v1.flatten()
    flattened_v2 = v2.flatten()
    dot_product = 0
    if not len(flattened_v1) == len(flattened_v2):
        raise Exception("input vectors are not of same length =(")
    return sum([v1_i * v2_i for v1_i, v2_i in zip(flattened_v1, flattened_v2)])

# 4.
# tumour_data = np.array([
#     [1, 17, 9],
#     [2, 21, 10],
#     [3, 12, 17]
# ])
tumour_data = np.array([
    [17, 9],
    [21, 10],
    [12, 17]
])

# 5.
# def summing_height_and_width(data):  # of tumour sizes, via a more efficent matrix multiplication than a for loop
# # timesing original matrix with [[0], [1], [1]] column vector allows for the id column to be ignored by the zero
# # and the values we do want (width and height) to be taken once by the 1s, and then subsequently for the width to
# # be added to their respective height
#     return (np.matmul(np.array([[0], [1], [1]]), data))  # matmul will automatically flip the array over to column vector form to suit the matrix multiplication
# # edit: actually, no, it does not

def summing_height_and_width(data):
    return (np.matmul(np.array([[1], [1]]), data))  # note the columnness of the vector and the order of the vector

# 6.

def h(x):
    ones = (np.array([1, 1, 1]).reshape(3, 1))  # or ones = np.array([1, 1, 1]).T
    transformed_data = np.append(x, ones, axis=1)
    hypothesis_matrix = np.array([
        4,
        5,
        -100
    ])
    return transformed_data @ hypothesis_matrix
