import numpy as np
import pylab
import random

# number of steps
n = 100000

# two arrays containing the x and y coordinates
x = np.zeros(n)
y = np.zeros(n)

# filling coordinates with random variables
for i in range(1, n):
    val = random.randint(1, 4)
    if val == 1:
        x[i] = x[i - 1] + 1
        y[i] = y[i - 1]
    elif val == 2:
        x[i] = x[i - 1] - 1
        y[i] = y[i - 1]
    elif val == 3:
        x[i] = x[i - 1]
        y[i] = y[i - 1] + 1
    else:
        x[i] = x[i - 1]
        y[i] = y[i - 1] - 1

# Plotting
pylab.title("Random Walk ($n = " + str(n) + "$ steps)")
pylab.plot(x, y)
pylab.savefig("rand_walk" + str(n) + ".png", bbox_inches="tight", dpi=600)
#pylab.show()
