import numpy as np

# Generate some random data
data = np.random.randn(2, 3)
data
# array([[-0.2047,  0.4789, -0.5194],
#        [-0.5557,  1.9658,  1.3934]])

data * 10

# array([[-2.0471,   4.7894,  -5.1944],
#        [-5.5573,  19.6578,  13.9341]])

data + data
# array([[-0.4094,  0.9579, -1.0389],
#        [-1.1115,  3.9316,  2.7868]])



arr1 = np.array([1, 2, 3], dtype=np.float64)
arr2 = np.array([1, 2, 3], dtype=np.int32)
arr1.dtype
# dtype('float64')

arr2.dtype
# dtype('int32')
