import numpy as np

Z = [[0,0,0,0,0,0], # What other ways are to create numpy arrays?
     [0,0,0,1,0,0],
     [0,1,0,1,0,0],
     [0,0,1,1,0,0],
     [0,0,0,0,0,0],
     [0,0,0,0,0,0]]

Z = np.array(Z)

print(Z.dtype) # Why it is int32 and not int64?
print(Z.shape)

A = Z[1:5,1:5]
A[0,0] = 9
print(Z)

print(Z.base is None)
print(A.base is Z)

print(1 + (2*Z + 3)) # Effects all elements of Z

# Z + Z[1:-1,1:-1] # This produces a ValueError related to broadcasting

print(Z + 1) # Adding a scalar to a matrix automatically broadcasts it
