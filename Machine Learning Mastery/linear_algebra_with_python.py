# Indexing, slicing and shaping in numpy

# One dimensional example
from numpy import array
list = list(range(16))

data1d = array(list)
print(data1d)
print(type(data1d))

## Two dimensional
list_of_lists = [[0, 1], [2, 3], [4, 5]]
data2d = array(list_of_lists)

print(data2d)
print(type(data2d))

# reshaping 1D arrays into 3d
print(data1d.reshape(data1d.shape[0], 1))
print(data1d.reshape(4, 4))

# reshaping 2d arrays into 3d
print(data2d.reshape((data2d.shape[0], data2d.shape[1], 1)))
print(data1d.reshape((4, 2, 2)))
