# Q1: An ant is on a rectangular grid with southwest-most point (0, 0) and northeast-most point (n x m). Starting at (0, 0), each time, the ant travels along a path walking north or east by a unit length on the grid with equal probability until it reaches (n, m). Define the deviation of a D path (from the straight path) as max(x/m - y/n, y/n - x/m) for all points (x, y) along the path.
# IDEAS
# 1. Calculate Ds first and take into account only the maximum
# 2. Create a probability grid and use that for the calculations
# 3. Create a probability of maximum deviation grid for the calculations
# 3. Introduce recursion and memoization
# 4. Bootstrap the samping
# 5. Use Divide and conquer

# Think about calculating the second, bigger case based on the first
# Think about using a running variance and recursive alg"
# - The deviations come continuously,
# Think about catastrophic cancellation problem

import time
t0 = time.time()

import numpy as np


teps = np.array([[1,0],[0,1]])

m = 1
n = 1

print("m, n: {}, {}".format(m, n))
shape = (n + 1, m + 1)

# Calculating probabilities
probs = np.zeros(shape)
probs[0,0] = 1

def calc_prob(array, axis=0):
    if axis == 1:
        array = array.T

    array[1] += array[0] / 2

    if len(array) > 2:
        calc_prob(array[-len(array) + 1:])

    return array

calc_prob(probs[0,:])
calc_prob(probs[:,0])

def calc_prob_step(array):
    # print("array:\n{}".format(array))
    if array.shape[1] > 2:
        array[1,1] = array[0,1] / 2 + array[1,0] / 2
        calc_prob_step(array[:,1:])
    elif array.shape[1] == 2:
        array[1,1] = array[0,1] + array[1,0] / 2
    else:
        return array

def calc_prob_axis(array):
    # print(array)
    if array.shape[0] > 2:
        calc_prob_step(array)
        calc_prob_axis(array[1:,:])

    if array.shape[0] == 2:
        array[1,1] = array[0,1] / 2 + array[1,0]
        if array.shape[1] > 3:
            calc_prob_axis(array[:,1:])
        else:
            array[-1,-1] = array[-2,-1] + array[-1,-2]
            return array

calc_prob_axis(probs)

# Calculating deviations
xs, ys = np.mgrid[0:shape[0], 0:shape[1]]
devs = np.maximum(xs / m - ys / n, ys / n - xs / m)

#print("probs:\n{}".format(probs))
print("devs:\n{}".format(devs))
print("probs:\n{}".format(probs))

def path(arr, shape):
    #grid = np.zeros((shape[0], shape[1]))
    D = 0

    cords = np.zeros((np.sum(shape) -1, 2)).astype(int)

    cords[1:] = steps[np.random.randint(0, 2, np.sum(shape) - 2)]
    cords[:, 0] = np.cumsum(cords[:,0])
    cords[:, 1] = np.cumsum(cords[:,1])

    cords[:, 0] = np.where(cords[:, 1] > shape[1] - 1,
                           cords[:,0] + cords[:,1] - shape[1] + 1,
                           cords[:,0])

    cords[:, 1] = np.where(cords[:, 0] > shape[0] - 1,
                           cords[:,1] + cords[:,0] - shape[0] + 1,
                           cords[:,1])

    cords[:, 0] = np.where(cords[:, 0] > shape[0] - 1,
                           shape[0] - 1,
                           cords[:,0])

    cords[:, 1] = np.where(cords[:, 1] > shape[1] - 1,
                           shape[1] - 1,
                           cords[:,1])

    #print("cords:\n{}".format(cords))

    first = (cords[:,0] / shape[0]) - (cords[:,1] / shape[1])
    #print("first:\n{}".format(first))
    second = (cords[:,1] / shape[1]) - (cords[:,0] / shape[0])

    D = max(max(first), max(second))
    #print("D:\n{}".format(D))

    #grid[cords[:, 0], cords[:, 1]] = 1
    #print("grid:\n{}".format(grid))
    #print("-" * 32)
    return D

def simulate(trials, shape, cond):
    d = np.hstack((np.zeros(shape[0] - 1), np.ones(shape[1] - 1))).astype(int)
    ds = np.tile(d, (trials, 1))

    DS = np.apply_along_axis(path, 1, ds, shape)
    #print("print(DS > {}):\n{}".format(cond[0], np.count_nonzero(DS > cond[0])))
    #print("print(DS > {}):\n{}".format(cond[1], np.count_nonzero(DS > cond[1])))

    DSm = DS.mean()
    DSs = DS.std()

    cprob = np.where((DS > cond[1]).any(), np.count_nonzero(DS > cond[0]) / np.count_nonzero(DS > cond[1]), 0)

    cprob = float(cprob)

    return DSm, DSs, cprob, DS


#What is the mean of D when m = 11 and n = 7?
#1.234567890
#What is the standard deviation D when m = 11 and n = 7?
#0.9876543210
#What is the conditional probability that D is greater than 0.6 given that it is greater than
#0.2 when m = 11 and  n = 7?
#1.234567890
# trials = 1000000
# print("Running with {} trials...".format(trials))
#
# m = 11
# n = 7
# cond_prob_par = (0.6, 0.2)
#
# mean, std, prob, DS = simulate(trials, shape, cond_prob_par)
# print("""\nsimulate: {} ({})
#          condprop: {}""".format(round(mean, 10),
#                                 round(std, 10),
#                                 round(prob, 10)))

#print("On a m = 11, n = 7 grid, and based on 100 000 simulations: 0.4650068831 (0.1599357116), condprop: 0.1953154438")

#What is the mean D when m = 23 and n = 31?
#1.234567890
#What is the standard deviation D when m = 23 and n = 31?
#0.9876543210
#What is the conditional probability that D is greater than 0.6 given that it is greater than
# 0.2 when m = 23 and n = 31?
#0.9876543210

# m = 23
# n = 31
# mean, std, prob, DS = simulate(trials, shape, cond_prob_par)
# print("""\nsimulate: {} ({})
         # condprob: {}""".format(round(mean, 10),
                                # round(std, 10),
                                # round(prob, 10)))

#print("On a m = 23, n = 31 grid, and based on 100 000 simulations: 0.3416129313 (0.1323430039), condprob: 0.0529353234")

#print("Duration of the program: {}".format(time.time() - t0))
