import numpy as np
import functools
from tempfile import mkdtemp

import sys
sys.setrecursionlimit(100000)

from joblib.memory import Memory
cache_dir = mkdtemp()
memory = Memory(location=cache_dir, verbose=0)


# Old solution
# @memory.cache
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
    # print("\nnewcs: {}".format(newcs))

    if T > 1 and len(newcs) > 3:
        return cut_rope(newcs, T-1)
    else:
        # print("\ncs: {}".format(newcs))
        S = len(newcs) + 1
        # print("S: {}".format(S))
        return S


# New solution
def check_doubles(cuts, ori, n=1):
    if cuts[cuts[:,0] == cuts[:,1]].any() == True and n>0:
        # print("cuts\n:{}".format(cuts))
        # print("-"*10)

        doubs = cuts[cuts[:,0] == cuts[:,1]]
        # print("doubs:\n{}".format(doubs))

        oridoubs = ori[cuts[:,0] == cuts[:,1]]
        arrcut(doubs, oridoubs)
        # cuts[cuts[:,0] == cuts[:,1]] = np.random.randint(ori[:,0], N, doubs.shape)
        # print("\nnew cuts:\n{}".format(doubs))
        return check_doubles(doubs, oridoubs, n-1)
    else:
        # print("cuts\n:{}".format(cuts))
        return cuts

def calc_lengths(cuts, ori):
    first = cuts[:,0] - ori[:,0] + 1
    second = np.abs(cuts[:,1] - cuts[:,0])
    third = ori[:,1] - cuts[:, 1] + 1
    return np.array([first, second, third]).T

def new_cuts(cuts, pos, ori):
    ncs = cuts.copy()
    ncs[:, 0][pos == 0] = ori[pos == 0][:,0]
    ncs[:, 1][pos == 0] = cuts[pos == 0][:, 0]
    ncs[:, 0][pos == 1] = cuts[pos == 1][:, 0] + 1
    ncs[:, 1][pos == 1] = cuts[pos == 1][:, 1] - 1
    ncs[:, 0][pos == 2] = cuts[pos == 2][:, 1]
    ncs[:, 1][pos == 2] = ori[pos == 2][:,1]
    return ncs

def arrcut(arr, ori):
    if arr.shape[0] > 0:
        # if np.diff(arr[0]) > 1 or np.diff(arr[0]) == 0:
        arr[0] = np.sort(np.random.randint(ori[0,0], ori[0,1] + 1, (1, 2)), axis=1)

        return np.vstack((arr[0], arrcut(arr[1:], ori[1:])))
    else:
        return arr

# @memory.cache
def cutter(arr, T, shorts):
    filter = (np.diff(arr) > 1).reshape(arr.shape[0],)
    shorts = np.vstack((shorts, arr[~filter]))
    arr = arr[filter]
    # print("\shorts.shape:\n{}".format(shorts.shape))

    print("*" * 20)
    # print("\narr.shape:\n{}".format(arr.shape))
    # print("\nNew round: {}.".format(T))

    ori = arr.copy()

    # print("\nori:\n{}".format(ori))
    arrcut(arr, ori)
    # print("cuts:\n{}".format(arr))

    # cuts = cut(N, n_trials)
    check_doubles(arr, ori)
    # ori = cuts.copy()
    ls = calc_lengths(arr, ori)
    # print("ls:\n{}".format(ls))
    pos = ls.argmax(axis = 1)
    # print("pos:\n{}".format(pos))

    nr = new_cuts(arr, pos, ori)
    # print("nr:\n{}".format(nr))

    if T > 1:
        return cutter(nr, T - 1, shorts)
    else:
        final = np.vstack((shorts, nr))
        # print("\nfinal.shape:\n{}".format(final.shape))
        return np.diff(final)


@memory.cache
def recmean(arr):
    # print("\narr: {}".format(arr))
    # print("(len(arr)): {}".format(len(arr)))
    if len(arr) > 1:
        n = len(arr)
        mean = ((n - 1) * recmean(arr[1:]) + arr[0]) / n
        # print("\nmean:\n{}".format(mean))
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
        # II = n / (n-1) * (arr.mean() - arr[0]) ** 2
        var = 1 / (n-1) * (I + II)
        return np.sqrt(var)
    else:
        # return 2 * (recmean(arr) - arr) ** 2
        return 0

@memory.cache
def recstat(arr):
    # print("narr: {}".format(arr))
    # print("(len(arr)): {}".format(len(arr)))

    if len(arr) > 1:
        n = len(arr)
        prev_mean, prev_var = recstat(arr[1:])
        # print("\nprev_mean, prev_var:\n{}, {}".format(prev_mean, prev_var))
        mean = ((n - 1) * prev_mean + arr[0]) / n

        I = (n-2) * prev_var ** 2
        II = n / (n-1) * (mean - arr[0]) ** 2
        var = 1 / (n-1) * (I + II)

        # print("nmean, var: {}, {}".format(mean, var))
        return mean, np.sqrt(var)
    else:
        return arr[0], 0


def bs(arr, n=100):
    # print("\narr for bs:\n{}".format(arr))
    arr.resize(len(arr))
    if n > 1:
        arr = np.random.choice(arr, len(arr))
        return bs(arr, n-1)
    else:
        return arr

def mean_lru(arr):
    print("Calculating mean and std...")
    # return recstat(arr)
    # return recmean(arr), recstd(arr)
    return arr.mean(), arr.std()

def trial_lru(N, T, n_trials, q, c):
    Ss = np.arange(0).reshape(0,2)
    cuts = np.tile(np.array([1, N - 1]), (n_trials, 1))

    # Ss = np.apply_along_axis(cut_rope, 1, t_cs, T) # Old solution
    Ss = dnq(cuts, T, Ss)
    # print("\nSs before bs:\n{}".format(Ss))
    Ss = bs(Ss)
    # print("\nSs after bs:\n{}".format(Ss))
    if np.sum(Ss > c) == 0:
        p = 0
    else:
        p = np.sum(Ss > q) / np.sum(Ss > c)

    return Ss, p


def dnq(cuts, T, Ss):
    print("\nremaining trials:\n{}".format(len(cuts)))
    if len(cuts) > 10000:
        return np.vstack((cutter(cuts[:10000,], T, Ss[:10000,]),
                         (dnq(cuts[10000:,], T, Ss[10000:,]))))
    else:
        # print("\ncuts.shape:\n{}".format(cuts.shape))
        return cutter(cuts, T, Ss)

n_trials = 10000
N, T = N1, T1 = 64, 5
N2, T2 = 1024, 10
q1, c1 = 8, 4
q2, c2 = 12, 6


print("\nRunning the first trial...")
Ss1, p1 = trial_lru(N1, T1, n_trials, q1, c1)
mean1, std1 = mean_lru(Ss1)

print("\n\n\nRunning the second trial...")
Ss2, p2 = trial_lru(N2, T2, n_trials, q2, c2)
mean2, std2 = mean_lru(Ss2)

print("\nIn the case of N=64 and T=5, and based on {} trials, the mean and the std are {} ({}) respectively. There is a {} probability of S being greater than 8, given that it is greater than 4.".format(n_trials, round(mean1, 11), round(std1, 11), round(p1, 11)))

print("\nIn the case of N=1024 and T=10, and based on {} trials, the mean and the std are {} ({}) respectively. There is a {} probability of S being greater than 12, given that it is greater than 6.".format(n_trials, round(mean2, 11), round(std2, 11), round(p2, 11)))
