# Vectorizing conditional loops

import numpy as np
from math import sin as sn
import matplotlib.pyplot as plt
import time

# Test points
N_point = 1000

# Original conditional function
def myfunc(x, y):
    if (x > 0.5 * y and y < 0.3):
        return (sn(x - y))
    elif (x < 0.5 * y):
        return 0
    elif (x > 0.2 * y):
        return (2 * sn (x + 2 * y))
    else:
        return (sn(y + x))

# Random distributions
lst_x = np.random.randn(N_point)
lst_y = np.random.randn(N_point)
lst_result = []

# Plotting the data
plt.hist(lst_x, bins=20)
plt.show()
plt.hist(lst_y, bins=20)
plt.show()

# First, plain vanilla for-loop
t1 = time.time()
for i in range(len(lst_x)):
    x = lst_x[i]
    y = lst_y[i]

    if (x > 0.5 * y and y < 0.3):
        lst_result.append(sn(x-y))
    elif (x < 0.5 * y):
        lst_result.append(0)
    elif (x > 0.2 * y):
        lst_result.append(2 * sn (x + 2 * y))
    else:
        lst_result.append(sn(y + x))
print("Time taken by plain for-loop:{} us".format(1000000 * (time.time() - t1)))

# List comprehension
t1 = time.time()
lst_result = [myfunc(x, y) for x, y in zip(lst_x, lst_y)]
print("Time taken by list coprehension and zip: {}".format(1000000 * (time.time() - t1)))

# Map() function
t1 = time.time()
list(map(myfunc, lst_x, lst_y))
print("Time taken by map function: {}".format(1000000 * (time.time() - t1)))

# Nympy vectorize method
t1 = time.time()
vectfunc = np.vectorize(myfunc, otypes=[np.float], cache=False)
list(vectfunc(lst_x, lst_y))
print("Time taken by numpy.vectorize method: {}".format(1000000 * (time.time() - t1)))
