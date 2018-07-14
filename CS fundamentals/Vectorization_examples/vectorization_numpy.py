import time
import numpy as np
x = np.linspace(-2., 2., 1000000)
print("x:\n{}".format(x))
print("np.sin(x):\n{}".format(np.sin(x)))
print("np.abs(x):\n{}".format(np.abs(x)))

# Original function
y = np.zeros(x.shape)

t1 = time.time()
for j in range(len(x)):
    if x[j] <= 0.5:
        y[j] = x[j]**2
    else:
        y[j] = -x[j]

print("Duration of the original for loop:\n{}".format(time.time() - t1))

# Rewriting the for loop with np.where
t1 = time.time()
y = np.where(x <= 0.5, x ** 2, -x)
print("Duration of `np.where()`:\n{}".format(time.time() - t1))

# Repeated use
t1 = time.time()
for j in range(len(x)):
    if x[j] <= 0.5:
        y[j] = x[j]**2

    elif x[j] < 1.5:
        y[j] = -x[j]

    else:
        y[j] = -x[j] ** 4

print("Duration of the multiple conditional:\n{}".format(time.time() - t1))

# Repeated np.where()
t1 = time.time()
y = np.where(x <= 0.5, x ** 2, -x)
y = np.where(x < 1.5, y, x ** 4)
print("Duration of the repeated `np.where()`:\n{}".format(time.time() - t1))

# Combining numpy boolean arrays
#print("(x >= 1) & (x <= 1.5):\n{}".format((x >= 1) & (x <= 1.5)))

# Properly we should use numpy logical operators
#print("np.logical_and(x >= 1 , x < 1.5):\n{}".format(np.logical_and(x>=1, x <= 1.5)))
