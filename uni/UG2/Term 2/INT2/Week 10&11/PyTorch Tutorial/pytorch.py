import torch as pt
import numpy as np

# tensors are a specialized data structure in pytorch, similar to arrays and matrices
data = [[1, 2],[3, 4]]
data_tensor = pt.tensor(data)

# attributes
data_tensor_shape = data_tensor.shape  # dimensions
data_tensor_datatype = data_tensor.dtype
data_tensor_stored_on_device = data_tensor.device

random_data_tensor = pt.rand_like(data_tensor)  # making tensor with random values of same shape and datatype as data_tensor
data_tensor_ones = pt.ones_like(data_tensor)  # same as above but with ones
data_tensor_zeros = pt.zeros_like(data_tensor)  # ditto but zeros

shape = (2,3,)  # creating tensors from specified dimensions
random_tensor = pt.rand(shape)
ones_tensor = pt.ones(shape)
zeros_tensor = pt.zeros(shape)

# can create pytorch tensor from numpy array and vice versa
# are stored in same memory often as well, so no need to copy between two datatypes
data_np_array = np.array(data_tensor)
data_tensor = pt.tensor(data_np_array)

# pytorch api is akin to numpy =)
# all operations can be run on GPU at higher speeds than CPU







