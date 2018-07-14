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
### Produces a scalar, the two vectors needs to be of the same shape
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
## Norm or magnitude: the length of the vector
a = array([1,2,3])
print(a.shape[0])

## L^1 Norm: the sum of the absolute values of the vector, or the Manhattan distance from the origin of the vector space
from numpy.linalg import norm
l1 = norm(a,1)
print(l1)

## L^2 Norm: the square root of the sum of squared vector values or the Euclidean distance from the origin
l2 = norm(a)
print(l2)

## Max Norm: the maximum value of the vector
from math import inf
maxnorm = norm(a, inf)
print(maxnorm)

# Matrices
A = array([
    [1, 2, 3],
    [4, 5, 6]
])
print("A:{}".format(A))

B = array([
    [1, 2, 3],
    [4, 5, 6]
])
print("B:{}".format(B))

C = A + B
print("C:{}".format(C))

D = A - B
print("D:{}".format(D))

E = A * B
print("E:{}".format(E))

F = A / B
print("F:{}".format(F))

## Matrix multiplication, or dot product
A = array([
    [1, 2],
    [3, 4],
    [5, 6]
])

B = array([
    [1, 2],
    [3, 4]
])

C = A @ B

print("A:{}".format(A))
print("B:{}".format(B))
print("C:{}".format(C))
print(C == A.dot(B))

## Matrix-vector multiplication
B = array([0.5, 0.5])
C = A.dot(B)
print("A:{}".format(A))
print("B:{}".format(B))
print("C:{}".format(C))

# Types of matrices
## Triangular matrices
from numpy import tril, triu
M = array([
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
])

lower = tril(M)
upper = triu(M)

print("M:\n{}".format(M))
print("lower:\n{}".format(lower))
print("upper:\n{}".format(upper))

## Diagonal matrix
from numpy import diag
d = diag(M)
print("d:\n{}".format(d))

## Identity matrix
from numpy import identity
I = identity(3)
print("I:\n{}".format(I))

## Orthogonal matrix
### Orthogonal vectors' dot product with each other is zero
### If their length is 1, they are also orthonormal

### An orthogonal matrix is a square matrix whose columns and rows are orthonormal unit vectors
### An orthogonal matrix's trnaspose is equal to its inverse
### An orthogonal matrix's dot product with its transpose is its identity matrix

from numpy.linalg import inv
Q = array([
    [1, 0],
    [0, -1]
])

V = inv(Q)
I = Q.dot(Q.T)

print("Q:\n{}".format(Q))
print("V:\n{}".format(V))
print("I:\n{}".format(I))

# Matrix operations
## Trace: The sum of the elements of the diagonal of a square matrix
from numpy import trace
A = array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

B = trace(A)
print("A:\n{}".format(A))
print("B:\n{}".format(B))

## Determinant: the volume of the matrix calculated as the product of the matrix's eigenvalues
from numpy.linalg import det
B = det(A)
print("B:\n{}".format(B))

## Rank: an estimation of the linearly independent directions of the matrix (e.g. 0 is a point, 1 is a line, 2 is a plane)
from numpy.linalg import matrix_rank

v1 = array([1, 2, 3])
vr1 = matrix_rank(v1)

v2 = array([0,0,0,0,0])
vr2 = matrix_rank(v2)

print("v1:\n{}".format(v1))
print("vr1:\n{}".format(vr1))
print("v2:\n{}".format(v2))
print("vr2:\n{}".format(vr2))

### Difference between dimensions and the number of linearly independent directions
M0 = array([
    [0, 0],
    [0, 0]
])

M1 = array([
    [1, 2],
    [1, 2],
])

M2 = array([
    [1, 2],
    [3, 4]
])

mr0 = matrix_rank(M0)
mr1 = matrix_rank(M1)
mr2 = matrix_rank(M2)

print("M0:\n{}".format(M0))
print("mr0:\n{}".format(mr0))
print("M1:\n{}".format(M1))
print("mr1:\n{}".format(mr1))
print("M2:\n{}".format(M2))
print("mr2:\n{}".format(mr2))

# Sparse matrix: they contain mostly zeros (which can be scored proportioniately)
## There are very useful when there is a huge feature space but with very few non-null values in itself.
## There are multiple ways to store the spare matrix form:
## 1. Dictonary of row and index values
## 2. List of lists
## 3. Tuples of row and column indexes and values
## Additionally, there are row and column compressed forms.

from scipy.sparse import csr_matrix
A = array([
    [1, 0, 0, 1, 0, 0],
    [0, 0, 2, 0, 0, 1],
    [0, 0, 0, 2, 0, 0]
])

S = csr_matrix(A)
B = S.todense()

print("A:\n{}".format(A))
print("S:\n{}".format(S))
print("B:\n{}".format(B))

## Calculating sparsity
from numpy import count_nonzero
sparsity = 1.0 - count_nonzero(A) / A.size
print("sparsity:\n{}".format(sparsity))

# Tensors: A generalization of matrices and vectors, or a multidimensional array
T = array([
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[11, 12, 3], [14, 15, 16], [17, 18, 19]],
    [[21, 22, 23], [24, 25, 26], [27, 28, 29]],
])

print("T.shape:\n{}".format(T.shape))
print("T:\n{}".format(T))

## Tensordot of a `q` and an `r` dimension tensors produces a new tensor with `q + r` dimension
from numpy import tensordot
A = array([1, 2])
B = array([3, 4])
C = tensordot(A, B, axes=0)
print("C:\n{}".format(C))

# Matrix decompositon: reducing a *square* matrix to its constituent parts
## LU decompositon: breaks down the matrix to a lower and an upper triangle matrix part

## LUP decompositon: same as the LU but it also
## 1. changes the order of the rows
## 2. creates also a 'P' component which reorders the rows

from scipy.linalg import lu
A = array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print("A:\n{}".format(A))

P, L, U = lu(A) # By default `lu()` does LUP
print("U:\n{}".format(U))
print("L:\n{}".format(L))
print("P:\n{}".format(P))

B = P.dot(L).dot(U)
print("B:\n{}".format(B))

## QR decompositon: Breaks down and n x m matrix to the dot product of an n x n square matrix and an n x m upper triangle matrix.
## The `qr()` method, by default, creates smaller dimension results, but with the 'complete' parameter we can make it to create the officially defined ones.
from numpy.linalg import qr

A = array([
    [1, 2],
    [3, 4],
    [5, 6],
])

Q, R = qr(A, 'complete')

print("A:\n{}".format(A))
print("Q:\n{}".format(Q))
print("R:\n{}".format(R))

B = Q.dot(R)

print("B:\n{}".format(B))

## Cholesky decompositon: Takes a square symmetric matrix with nonzero values ('positive definite matrix') and breaks it down into the dot product of a lower triangle matrix and its transpose (A = LL^T) or of the transpose of an upper triangle matrix and itself (A = U^T U)
from numpy.linalg import cholesky
A = array([
    [2, 1, 1],
    [1, 2, 1],
    [1, 1, 2],
])

print("A:\n{}".format(A))

L = cholesky(A)
print("L:\n{}".format(L))
B = L.dot(L.T)
print("B:\n{}".format(B))

# Eigendecomposition
## The eigenvector of a matrix, is a vector which, if multiplied by a scalar (the eigenscalar) produces the vectors product with the original matrix.
## A * v = s * v

## * Not all matrix has eigenvalues
## * Some matrixes can be eigendecomposed only by complex numbers
## * A matrix can have as much eigencomponents as its dimensions

## A matrix can be also described by its all eigencomponents
## A = Q * R * Q^T, where
## - Q is the matrix of the eigenvectors
## - R is a diagonal matrix where the values of the diagonal are the eigenvalues

## positive and negative definite matrices of those whose all eigenvalues are either positive or negative respectively

from numpy.linalg import eig

A = array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
])

print("A:\n{}".format(A))
values, vectors = eig(A)

print("values:\n{}".format(values))
print("vectors:\n{}".format(vectors))

## Checking the validity of an eigenvector
B = A.dot(vectors[:, 0])
C = vectors[:, 0] * values[0]

print("B:\n{}".format(B))
print("C:\n{}".format(C))

## Reconstructing the original matrix
D = vectors.dot(diag(values).dot(inv(vectors)))
print("D:\n{}".format(D))

# Singular Value Decomposition
## This can be created for any kind of matrix
## This decomposes an m x n matrix into the following form:
## A = U * Sigma * V^T, where
## * U is an m x m matrix, its columns are the right-singular vectors
## * Sigma is an m x n diagonal matrix composed of the singular values of the matrix
## * V is an n x n matrix, its columns are the left-singular vectors

from scipy.linalg import svd

A = array([
    [1, 2],
    [3, 4],
    [5, 6],
])

print("A:\n{}".format(A))
U, s, V = svd(A)
print("U:\n{}".format(U))
print("s:\n{}".format(s))
print("V:\n{}".format(V))

## Reconstructing the original matrix
## Because the original matrix is not square shaped, the diagonal matrix of the singular values needs to be complemented by the columns or rows of zeros

Sigma = zeros((A.shape[0], A.shape[1]))
#Sigma[:A.shape[1], :A.shape[1] - diag(s)]
Sigma[:len(s), :len(s)] = diag(s)

B = U.dot(Sigma.dot(V))
print("B - A:\n{}".format(B - A))

## Pseudoinverse
### Rectangualr matrices do not have inveres, but can have a pseudoinverse matrix which we can get in the following way:
### A^+ = V * D^+ * U.T where
### * D^+ is the pseudoinverse of Sigma, that is, the A matrix's singular value diagonal matrix
### * U and V are the corresponding SVD components of the A matrix

### Sigma's pseudoinverse is a diagonal matrix of its transposed shape and with its reciprocals values.

from numpy.linalg import pinv
A = array([
    [0.1, 0.2],
    [0.3, 0.4],
    [0.5, 0.6],
    [0.7, 0.8],
])

print("A:\n{}".format(A))
B = pinv(A)
print("B:\n{}".format(B))

U, s, V = svd(A)
print("U:\n{}".format(U))
print("s:\n{}".format(s))
print("V:\n{}".format(V))

#Sigma = zeros((A.shape[0], A.shape[1]))
#Sigma[:len(s), :len(s)] = diag(s)
#print("Sigma:\n{}".format(Sigma))

Sigma_pinv = zeros((A.shape[1], A.shape[0]))
Sigma_pinv[:len(s), :len(s)] = diag(1/s)
print("Sigma_pinv:\n{}".format(Sigma_pinv))

B = V.T @ Sigma_pinv @ U.T
print("B - pinv(A):\n{}".format(B - pinv(A)))

# Dimensionality reduction
A = array(range(1, 31)).reshape(3, 10)
print("A:\n{}".format(A))

U, s, V = svd(A)
# print("U:\n{}".format(U))
# print("s:\n{}".format(s))

Sigma = zeros((A.shape[0], A.shape[1]))
Sigma[:len(s), :len(s)] = diag(s)

n_elements = 2
Sigma = Sigma[:, :n_elements]
V = V[:n_elements, :]
# print("Sigma:\n{}".format(Sigma))
# print("V:\n{}".format(V))

B = U.dot(Sigma.dot(V))
print("B:\n{}".format(B))

T = U.dot(Sigma)
print("T = U.dot(Sigma):\n{}".format(U.dot(Sigma)))
print("T = A.dot(V.T):\n{}".format(A.dot(V.T)))

### Using scikit-learn's `TruncatedSVD` function
from sklearn.decomposition import TruncatedSVD
print("A:\n{}".format(A))

svd = TruncatedSVD(n_components=n_elements)
svd.fit(A)
result = svd.transform(A)
print("result:\n{}".format(result))
