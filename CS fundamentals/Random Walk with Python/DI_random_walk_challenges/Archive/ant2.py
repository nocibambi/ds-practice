# Q1: An ant is on a rectangular grid with southwest-most point (0, 0) and northeast-most point (n x m). Starting at (0, 0), each time, the ant travels along a path walking north or east by a unit length on the grid with equal probability until it reaches (n, m). Define the deviation of a D path (from the straight path) as max(x/m - y/n, y/n - x/m) for all points (x, y) along the path.
import time
t0 = time.time()
import numpy as np

def path(arr, shape):
    #grid = np.zeros((shape[0], shape[1]))
    D = 0

    h = np.random.permutation(arr)
    v = 1 - h

    cords = np.array((np.cumsum(v), np.cumsum(h))).T
    cords = np.vstack(([0,0], cords))

    first = (cords[:,0] / shape[0]) - (cords[:,1] / shape[1])
    #print("first:\n{}".format(first))
    second = (cords[:,1] / shape[1]) - (cords[:,0] / shape[0])


    D = max(max(first), max(second))
    #print("D:\n{}".format(D))

    #grid[cords[:,0], cords[:, 1]] = 1
    #print("grid:\n{}".format(grid))
    #print("-" * 32)

    return D

def simulate(trials, shape, cond):
    ##########
    # TRY PERHAPS WITH EQUAL PROBS AND BORDERS INSTEAD?
    ##########

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
import time
t0 = time.time()

trials = 100000
cond_prob_par = (0.6, 0.2)

shape1 = (11, 7)

mean, std, prob, DS = simulate(trials, shape1, cond_prob_par)
print("""\nsimulate: {} ({})
         condprop: {}""".format(round(mean, 10),
                                round(std, 10),
                                round(prob, 10)))

#print("On a m = 11, n = 7 grid, and based on 100 000 simulations: 0.4650068831 (0.1599357116), condprop: 0.1953154438")

#What is the mean D when m = 23 and n = 31?
#1.234567890
#What is the standard deviation D when m = 23 and n = 31?
#0.9876543210
#What is the conditional probability that D is greater than 0.6 given that it is greater than
# 0.2 when m = 23 and n = 31?
#0.9876543210

#shape2 = (23, 31)
# mean, std, prob, DS = simulate(trials, shape2, cond_prob_par)
# print("""\nsimulate: {} ({})
#          condprob: {}""".format(round(mean, 10),
#                                 round(std, 10),
#                                 round(prob, 10)))

#print("On a m = 23, n = 31 grid, and based on 100 000 simulations: 0.3416129313 (0.1323430039), condprob: 0.0529353234")

import time
t0 = time.time()
