# Numpy arrays
from numpy import array
l = [1.0, 2.0, 3.0]
a = array(l)

print(a.shape)
print(a.dtype)

## Creating arrays with functions
from numpy import empty
a = empty([3, 3])
print(a)

## Zeros
from numpy import zeros
a = zeros([3, 5])
print(a)

## Ones
from numpy import ones
a = ones([2, 4])
print(a)

# Combining arrays
## Vertical stack
from numpy import vstack

a1 = array([1, 2, 3])
print(a1)
a2 = array([4, 5, 6])
print(a2)

a3 = vstack((a1, a2)) # Vertical stack
print(a3)
print(a3.shape)

## Horizontal stack
from numpy import hstack
a1 = array([1, 2, 3])
print(a1)
a2 = array([4, 5, 6])
print(a2)

a3 = hstack((a1, a2))
print(a3)
print(a3.shape)

# One dimensional example
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

# Numpy broadcasting
## Scalar and One-Dimensional array
a = array([1, 2, 3])  # define array
print(a)

b = 2 # define scalar
print(b)

c = a + b
print(c)

## Scalar and One-Dimensional array
A = array([
    [1, 2, 3],
    [1, 2, 3]])
print(A)

b = 2
print(b)

C = A + b
print(C)

## One- and Two-dimensional arrays
A = array([
[1, 2, 3],
[1, 2, 3]])
print(A)

b = array([1, 2, 3])
print(b)

C = A + b
print(C)

# Numpy performs arithmetic only when
# 1. the shape of each dimension in the arrays are equal, or
# 2. One has a non-trailing dimension size of 1

# Trailing dimension: The last dimension in their order, e.g. for a two dimension matrix, the column.
# Error example:

#A = array([
#[1, 2, 3],
#[1, 2, 3]])
#print(A.shape)
## define one-dimensional array
#b = array([1, 2])
#print(b.shape)
## attempt broadcast
#C = A + b
#print(C)

# Vectors and Vector arithmetic
v = array([1, 2, 3])

## Simple vector arithmetic: element-wise operations between vectors of the
# resulting in a new vector of the same length

### Addition
a = array([1,2,3])
b = array([1,2,3])
c = a + b
print(c)

### Subtraction
d = array([0.5, 0.5, 0.5])
print(c - d)
print(a - d)

### Multiplication
print(a * b)
print(a * c)
print(a * d)
print(c * d)

### Division
print(a / b)
print(c / a)
print(d / a)
print(c / d)

### Vector dot product
e = a.dot(b)
f = a.dot(c)
g = a.dot(d)
h = a.dot(e)
print(e)
print(f)
print(g)
print(h)

### Vector-scalar Multiplication
s = 0.5
i = c * s
print(i)

# Vector norm
## L^1 Norm

from numpy.linalg import norm
a = array([1,2,3])
l1 = norm(a,1)
print(l1)

## L^2 Norm
l2 = norm(a)
print(l2)

## Max Norm
from math import inf
maxnorm = norm(a, inf)
print(maxnorm)
