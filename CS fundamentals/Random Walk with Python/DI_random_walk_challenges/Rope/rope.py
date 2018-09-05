# There is a rope of length N with points at interior integer coordinates (1,…,N−1).
# At every turn, we select 2 unique interior integer coordinates uniformly at random without replacement, cut the rope at those 2 coordinates, and take the longest of the resulting 3 ropes as our new rope.
# We do this iteratively T times (as long as it is possible to cut the rope at 2 unique interior coordinates) and call the length of the final resulting rope S

import numpy as np
import functools
import sys
from tempfile import mkdtemp

sys.setrecursionlimit(100000)

from joblib.memory import Memory
cache_dir = mkdtemp()
memory = Memory(location=cache_dir, verbose=0)

# @functools.lru_cache(maxsize=None)
@memory.cache
def cut_rope(cs, T):
    # print("-" *8 + "\nT: {}.".format(T))
    # print("\ncs: {}".format(cs))
    i, j = np.sort(np.random.choice(np.arange(len(cs)), size=2, replace=False))
    # print("\ni, j: {}, {}".format(i, j))
    x, y = cs[i], cs[j]
    # print("x, y: {}, {}".format(x, y))
    #
    # print("\n0: {} - 0 - 1: {}".format(x, x - cs[0] + 1))
    # print("1: {} - {}: {}".format(y, x, y - x))
    # print("2: {} + 1 - {}: {}".format(cs[-1], y, cs[-1] + 1 - y))

    choice = np.argmax([x - cs[0] + 1, np.abs(y - x), cs[-1] + 1 - y])
    # print("choice: {}".format(choice))
    # In case there are more than one rope with the same maximum length, we simply choose the first, because their specific content is not relevant.

    newr = np.where(choice==0,
                  (cs[0], x),
                  np.where(choice==1,
                           (x + 1, y - 1),
                           (y + 1, cs[-1])))
    # print("\nnewr: {}".format(newr))

    newcs = np.arange(newr[0], newr[1])
    print("\nnewcs: {}".format(newcs))

    if T > 1 and len(newcs) > 3:
        return cut_rope(newcs, T-1)
    else:
        # print("\ncs: {}".format(newcs))
        S = len(newcs) + 1
        # print("S: {}".format(S))
        return S






@memory.cache
def recmean(arr):
    # print("\narr: {}".format(arr))
    # print("(len(arr)): {}".format(len(arr)))
    n = len(arr)
    if len(arr) > 1:
        mean = ((n - 1) * recmean(arr[1:]) + arr[0]) / n
        return mean
    else:
        return arr[0]

@memory.cache
def recstd(arr):
    # print("arr: {}".format(arr))
    # print("len(arr): {}".format(len(arr)))
    if len(arr) > 1:
        n = len(arr)
        I = (n-2) * recstd(arr[1:]) ** 2
        II = n / (n-1) * (recmean(arr) - arr[0]) ** 2
        var = 1 / (n-1) * (I + II)
        return np.sqrt(var)
    else:
        # return 2 * (recmean(arr) - arr) ** 2
        return 0

@memory.cache
# @functools.lru_cache(maxsize=None)
def mean_lru(arr):
    # print("Calculating mean and std...")
    # return recmean(arr), recstd(arr)
    return arr.mean(), arr.std()

# @memory.cache
@functools.lru_cache(maxsize=None)
def trial_lru(N, T, n_trials, q, c):

    # ts = np.ones(n_trials)
    # cs = np.arange(1, N)
    t_cs = np.tile(np.arange(1, N), (n_trials, 1))
    # def trials(tcs, T):
    #     if len(t_cs) > 1:
    #         return np.hstack((cut_rope(t_cs[0], T), trials(t_cs[1:], T)))
    #     else:
    #         return cut_rope(t_cs[0], T)
    #
    # SS = trials(t_cs, T)
    Ss = np.apply_along_axis(cut_rope, 1, t_cs, T)

    if np.sum(Ss > c) == 0:
        p = 0
    else:
        p = np.sum(Ss > q) / np.sum(Ss > c)
    # p = np.nan
    return Ss, p

# @memory.cache
# def sim(arr, N, T):
#     if len(arr) > 1:
#         cs = np.arange(1, N)
#         D = cut_rope(cs, T)
#         # print("arr: {}".format(arr))
#         # print("D: {}".format(D))
#         arr[0] = D
#         return sim(arr[1:], N, T)
#     else:
#         return arr

# def cuts(ts):
#     cs = np.arange(1, len(ts))
#     return cs

n_trials = 1000
N, T = N1, T1 = 64, 5
N2, T2 = 1024, 10
q1, c1 = 8, 4
q2, c2 = 12, 6

ts1 = np.ones(n_trials)
ts2 = np.ones(n_trials)

# ts = np.ones((n_trials, N))
# tst = np.apply_along_axis(cuts, 1, ts)
# tst = np.apply_along_axis(cut_rope, 1, tst, T)
# print("tst: {}".format(tst))

print("\nRunning the first trial...")
ts1, p1 = trial_lru(N1, T1, n_trials, q1, c1)
# np.apply_along_axis(sim, 0, ts1, N1, T1)
# print("ts1: {}".format(ts1))
mean1, std1 = mean_lru(ts1)

print("\nIn the case of N=64 and T=5, and based on {} trials, the mean and the std are {} ({}) respectively. There is a {} probability of S being greater than 8, given that it is greater than 4.".format(n_trials, round(mean1, 11), round(std1, 11), round(p1, 11)))
#4.721682 (2.4347531889)
#4.73088 (2.4302004908), 0.20198180722
#4.715565 (2.4310063206), 0.20177864828
# (2.4382408784), 0.20207144367
#4.7100825 (2.4198533723), 0.19918411136
#4.713106 (2.4243097642), 0.2007330392
#4.71754 (2.429946436).0.20168000669


print("\nRunning the second trial...")
ts2, p2 = trial_lru(N2, T2, n_trials, q2, c2)
# np.apply_along_axis(sim, 0, ts2, N2, T2)
# print("ts2: {}".format(ts2))
mean2, std2 = mean_lru(ts2)

print("\nIn the case of N=1024 and T=10, and based on {} trials, the mean and the std are {} ({}) respectively. There is a {} probability of S being greater than 12, given that it is greater than 6.".format(n_trials, round(mean2, 11), round(std2, 11), round(p2, 11)))
#6.72159 (5.5810570569)
#6.74626 (5.6790277348), 0.32738975385
#6.71771 (5.61774619896) 0.32295363314
#6.71300666667 (5.64927029152), 0.32752545027
#6.7108975 (5.63495627707), 0.32729328497
#6.709902 (5.64438385924), 0.32557308688
#6.71548833333 (5.61996780342) 0.32554627907

# What is the mean of S when N=64 and T=5
# What is the standard deviation of S when N=64 and T=5
# What is the mean of S when N=1024 and T=10
# What is the standard deviation of S when N=1024 and T=10
# What is the conditional probability that S is greater than 8 given that it is greater than 4 when N=64 and T=5
# What is the conditional probability that S is greater than 12 given that it is greater than 6 when N=1024 and T=10

# mean_lru.cache_clear()
# trial_lru.cache_clear()
