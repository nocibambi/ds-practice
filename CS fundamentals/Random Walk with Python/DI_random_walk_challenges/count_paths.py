import numpy as np
m = 2
n = 2

shape = (n + 1, m + 1)

grid = np.zeros(shape)

def count_right(array):
    if array.shape[1] > 0:
        array[0,:] += 1
        print("\n{}".format(array))
        count_down(array[1:,])
    else:
        return count_right(array[:-1,:])

def count_down(array):
    if array.shape[0] > 0:
        array[:,0] += 1
        print("\n{}".format(array))
        count_right(array[:,1:])
    else:
        return count_right(array[:,:-1])




# def count_paths(array):
#
#     if array.shape[1] > 0 :
#         array[0,:] += 1
#         print("\n{}".format(array))
#
#         if array.shape[0] > 0:
#             array[1:,-1] += 1
#             print("\n{}".format(array))
#
#         array[0,:-1] += 1
#         print("\n{}".format(array))
#
#         if array.shape[0] > 0:
#             array[1:,-2] += 1
#             print("\n{}".format(array))
#
#         array[-1,-1:] +=1
#         print("\n{}".format(array))
#
#         array[0,:2] +=1
#         print("\n{}".format(array))
#
#         if array.shape[0] > 0:
#             array[1,-2:] += 1
#             print("\n{}".format(array))
#
#         array[-1,-1] +=1
#         print("\n{}".format(array))


count_right(grid)
print("grid:\n{}".format(grid))


# def doubles(array):
#     grid[0,0] += 1
#     print("\n{}".format(array))
#
#     if array.shape[1] > 0:
#         print("grid.shape: {}".format(grid.shape))
#         return doubles(array[:,1:])
#
#         #if array.shape[0] > 0:
#         #    array[1,0] += 1
#         #    print("\n{}".format(array))
#
#
#         # return count_paths(array[:-1,:])
#         # array[1:,-2] += 1
