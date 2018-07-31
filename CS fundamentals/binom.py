import numpy as np
import time
import functools

np.random.seed(42)
samples = np.random.randint(0,2,10000)


print("\nSimulating mean and STD of binomial dist with numpy")

t1 = time.time()
np.mean(samples)
print("Duration of np.mean(samples): {}".format(time.time() - t1))
# 30.5 µs ± 470 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

t1 = time.time()
np.std(samples)
print("Duration of np.std(samples)): {}".format(time.time() - t1))
# 94.4 µs ± 442 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

t1 = time.time()
samples.mean()
print("Duration of samples.mean(): {}".format(time.time() - t1))
# 30.5 µs ± 470 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

t1 = time.time()
samples.std()
print("Duration of samples.std(): {}".format(time.time() - t1))
# 94.4 µs ± 442 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)

# Recurstions
print("\n\nRecursions\n")


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
        print("n: {}".format(n))
        print("0.5")
        return 0.5
    else:
        avgh = average_heads_m(n-1)
        print("\n")
        print("n: {}".format(n))
        avgh_mean = np.mean([avgh + 1./n, avgh - 1./n])
        print("avgh_n-1: {}".format(avgh + 1./n))
        print("avgh_n+1: {}".format(avgh - 1./n))
        print("1/n: {}".format(1./n))
        print("np.mean([avgh + 1./n, avgh - 1./n]): {}".format(avgh_mean))

        return avgh_mean


print("-"*20)

t1 = time.time()
avg_hds = average_heads_m(10)
print("-"*20)
print("Duration of average_heads(10), memoized: {}".format(time.time() - t1))

print("\nThe average number of heads: {}".format(avg_hds))
