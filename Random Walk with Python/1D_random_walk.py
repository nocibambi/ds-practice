# Based on https://www.cdn.geeksforgeeks.org/random-walk-implementation-python/

import random
import numpy as np
import matplotlib.pyplot as plt

# Probabilities to move up or down
prob = [0.5, 0.5]

# Defining the starting position
start = 2
positions = [start]

# createing the random points
rr = np.random.random(10)
downp = rr < prob[0]
upp = rr > prob[1]

for idown, iupp in zip(downp, upp):
    print(positions)
    down = idown and positions[-1] > 1
    print(down)
    up = iupp and positions[-1] < 4
    print(up)
    positions.append(positions[-1] - down + up)

# plotting down the graph of the random walk in 1D

plt.plot(positions)
#plt.show(figsize = (24, 24))
