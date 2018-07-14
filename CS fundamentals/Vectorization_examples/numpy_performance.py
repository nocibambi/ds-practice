import operator
import numpy as np
import time

a = np.random.randn(1000000)
b = np.random.randn(1000000)


# Simple addition
t1 = time.time()
c0 = a + b
print("Duration of a + b:\n{}".format(time.time() - t1))

# Operator.add()
t1 = time.time()
c1 = operator.add(a, b)
print("Duration of operator.add():\n{}".format(time.time() - t1))

# Using np.vectorize()
t1 = time.time()
c2 = np.vectorize(operator.add)(a, b)
print("Duration of np.vectorize():\n{}".format(time.time() - t1))

# Using np.add(a, b)
t1 = time.time()
c4 = np.add(a, b)
print("Duration of `np.add(a, b)`:\n{}".format(time.time() - t1))

print("(c0 == c4).all():\n{}".format((c0 == c4).all()))

#"So, the key to using NumPy is simple: it's not about moving the inner loop into NumPy, it's about getting rid of all Python functions in that inner loop. Only call natively-vectorized functions like np.add, or use operators like +, on the arrays."

#"This is where NumPy programming becomes an art rather than just literal translation. You have to learn all the functions NumPy includes, and get to know which ones to reach for when facing each problem, and the only way to get there is through experience."

# The original works with lists of lists
# for i, ra in enumerate(a):
#         c.append([])
#         for j, ca in enumerate(ra):
#             c[-1].append(ca + b[j][i] * i)
#
# c = a + b.T * np.arange(a.shape[0])
