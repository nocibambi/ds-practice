# 1. Vectorized Linear algebra
import numpy as np
import time
import functools

x = np.random.randn(1000000)
y = np.random.randn(1000000)

# First versions: simple loop
t1 = time.time()
z1 = sum(x[i] * y[i] for i in range(len(x)))
print("Duration of sum(x[i] * y[i] for i in range(len(x))): {}".format(time.time() - t1))
# 521 ms ± 5.28 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)


# Using numpy's dot product
t1 = time.time()
z2 = np.dot(x, y) # elapsed time: 0.0045 seconds
print("Duration of np.dot(x, y): {}".format(time.time() - t1))
# 2.69 ms ± 88.8 µs per loop (mean ± std. dev. of 7 runs, 1 loop each)

print("z1 - z2: {}".format(z1 - z2))
# 2.546585164964199e-11

####
# 2. Simulation
# Finding the mean and standard deviatoion of the number of heads after 10000 coin flips
np.random.seed(42)
samples = np.random.randint(0,2,10000)


print("\n\nMean and STD of binomial dist with numpy")

t1 = time.time()
np.mean(samples)
print("Duration of samples.mean(): {}".format(time.time() - t1))
# 30.5 µs ± 470 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

t1 = time.time()
np.std(samples)
print("Duration of samples.std(): {}".format(time.time() - t1))
# 94.4 µs ± 442 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

####
# 3. Recursion
print("\n\nRecursions")
# Fibonacci loop
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

t1 = time.time()
fib(30)
print("Duration of fib(30): {}".format(time.time() - t1))
# 493 ms ± 10.3 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)

# Average number of heads
# Solving the above coin flipping problem with recursion
def average_heads(n):
    if n == 1:
        return 0.5
    else:
        return np.mean([average_heads(n-1) + 1./n, average_heads(n-1) - 1./n])

# Takes a lot of time even for 10 flips
t1 = time.time()
average_heads(10)
print("Duration of average_heads(10): {}".format(time.time() - t1))
# 11 ms ± 85.3 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)


@functools.lru_cache()
def average_heads_m(n):
    if n == 1:
        return 0.5
    else:
        print("-"*20)
        print("average_heads_m(n-1):\n{}".format(average_heads_m(n-1)))
        print("average_heads_m(n-1):\n{}".format(average_heads_m(n-1)))
        print("1./n:\n{}".format(1./n))
        print("average_heads_m(n-1) + 1./n, average_heads_m(n-1) - 1./n:\n{}".format(average_heads_m(n-1) + 1./n, average_heads_m(n-1) - 1./n))
        print("np.mean([average_heads_m(n-1) + 1./n, average_heads_m(n-1) - 1./n]):\n{}".format(np.mean([average_heads_m(n-1) + 1./n, average_heads_m(n-1) - 1./n])))
        return np.mean([average_heads_m(n-1) + 1./n, average_heads_m(n-1) - 1./n])

t1 = time.time()
average_heads_m(10)
print("Duration of average_heads(10), memoized: {}".format(time.time() - t1))


# Graph traversal algorithm
print("Graph traversal algorithm")
# How many ways are there to get a given number by drawing coins and summing their values (if the order counts as well)?

coins = [1, 5, 10, 25, 50]
def count(remainder):
    if remainder < 0:
        return 0
        if remainder == 0:
            return 1
        return sum(count(remainder - coin) for coin in coins)

t1 = time.time()
count(50)
print("Duration of count(50):{}".format(time.time() - t1))

####
# 4. Memoization
## Manually
known = {0:1, 1:1}
def fib_man(n):
    if n in known:
        return known[n]
    else:
        known[n] = fib_man(n-2) + fib_man(n-1)
        return known[n]

## With decorator: DOES NOT WORK?
# @memoized Does not work

@functools.lru_cache()
def fib_dec(n):
    if n < 2:
        return 1
    else:
        return fib_dec(n-2) + fib_dec(n-1)

t1 = time.time()
fib_man(30)
print("Duration of manual memoization, fib_man(30): {}".format(time.time() - t1))
# 269 ns ± 1.22 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

t1 = time.time()
fib_dec(30)
print("Duration of functools memoization, fib_dec(30): {}".format(time.time() - t1))
# 204 ns ± 3.01 ns per loop (mean ± std. dev. of 7 runs, 1000000 loops each)

####
# 5. Divide and conquer
M = np.matrix([[1,1], [1,0]])

def fib_dc(n):
    if n < 2:
        return 1

    MProd = M.copy()
    for _ in range(n-2):
        MProd *= M

    return MProd[0,0] + MProd[0,1]

t1 = time.time()
fib_dc(30)
print("Duration of, divide an conquer fib_dc(30): {}".format(time.time() - t1))
# 330 µs ± 1.83 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
