# Q1: An ant is on a rectangular grid with southwest-most point (0, 0) and northeast-most point (n x m). Starting at (0, 0), each time, the ant travels along a path walking north or east by a unit length on the grid with equal probability until it reaches (n, m). Define the deviation of a D path (from the straight path) as max(x/m - y/n, y/n - x/m) for all points (x, y) along the path.
# import timeit
import time
t0 = time.time()
import numpy as np

def makegrid(shape):
    return np.zeros((shape[0], shape[1]))

def deviate(point, shape):
    first = point[0] / shape[0] - point[1] / shape[1]
    second = point[1] / shape[1] - point[0] / shape[0]
    return max(first, second)

#def deviate(point, shape):
#    first = point[0] / shape[1] - point[1] / shape[0]
#    second = point[1] / shape[0] - point[0] / shape[1]
#    return max(first, second)

def path(grid, shape):
    cord = np.array([0,0])
    grid[cord[0],cord[1]] = 1
    #shape = grid.shape

    cords = np.array([0,0])
    moves = np.array([[1,0],[0,1]])
    D = 0


    # newgrid = grid[cord[0]:, cord[1]:]
    # np.random.choice(np.arange(16), replace=False, size=6)

    for i in range(shape[0] + shape[1] - 2):
        if (cord[0] <= shape[0] - 2) & (cord[1] <= shape[1] - 2):
            cord += moves[np.random.randint(0,2)]
        elif cord[1] == shape[1] - 1:
            cord += moves[0]
        else:
            cord += moves[1]

        D = max(D, deviate(cord, shape))
        grid[cord[0],cord[1]] = 1
        cords = np.vstack((cords,cord))

    # print("grid: {}".format(grid)))
    return cords, D

def simulate(N, shape, condprob):
    grid = np.empty(0)
    grid = makegrid(shape)

    #Dsum = np.empty(0)
    Dsum = []
    cond = 0
    freq = 0

    for i in range(N):
        route, D = path(grid, shape)
        # print(D)
        Dsum.append(D)

        if D > condprob[1]:
            cond += 1
            if D > condprob[0]:
                freq += 1

    if cond == 0:
        cprob = 0
    else:
        cprob = freq/cond

    return np.mean(Dsum), np.std(Dsum), cprob

#What is the mean of D when m = 11 and n = 7?
#1.234567890
#What is the standard deviation D when m = 11 and n = 7?
#0.9876543210
#What is the conditional probability that D is greater than 0.6 given that it is greater than
#0.2 when m = 11 and  n = 7?
#1.234567890
trials = 100000
cond_prob_par = (0.6, 0.2)
shape1 = (11, 7)

mean, std, prob = simulate(trials, shape1, cond_prob_par)
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

# mean, std, prob = simulate(trials, (23, 31), cond_prob_par)
# print("""\nsimulate: {} ({})
         # condprob: {}""".format(round(mean, 10),
                                # round(std, 10),
                                # round(prob, 10)))

#print("On a m = 23, n = 31 grid, and based on 100 000 simulations: 0.3416129313 (0.1323430039), condprob: 0.0529353234")
print("Duration of the program: {}".format(time.time() - t0))
