from timeit import Timer
import numpy as np
import math

def timer(*funcs):
    """Find the maximum function name length, then run each function 1000 times and print stats"""
    if len(funcs) > 1:
        maxlen = max(*[len(func) for func in funcs])
    elif len(funcs) == 1:
        maxlen = len(funcs[0])
    else:
        return

    times = []
    print("--")
    for func in funcs:
        timerfunc = Timer("%s()" % func, "from __main__ import %s" % func)
        # Here the the Timer function runs a python command (added as a string, it also )
        runtime = timerfunc.repeat(repeat=10000, number=1)
        mtime = np.mean(runtime)
        stime = np.std(runtime)
        dfunc = func + (" " * (maxlen - len(func) + 1))
        print("%s: %.6f +/- %.6f seconds" % (dfunc, mtime, stime))

# Creating a list of numbers
def numpy_arange():
    l = np.arange(1000)

def py_list_comp():
    l = [i for i in range(1000)]

def py_range():
    l = list(range(1000))

timer("numpy_arange", "py_range", "py_list_comp")

def arange_to_list():
    l = list(np.arange(1000))

def py_list_comp_to_array():
    l = np.array(range(1000))

def py_range_to_ndarray():
    l = np.array([i for i in range(1000)])

timer("arange_to_list", "py_range_to_ndarray", "py_list_comp_to_array")


# Operations
def numpy_sum():
    total = np.sum(np.arange(1000))

def loop_sum():
    total = 0
    for i in range(1000):
        total += 1

timer("numpy_sum", "loop_sum")

def numpy_mean():
    mean = np.mean(np.arange(1000))

def loop_mean():
    """Sum all the numbers and calculate the mean"""
    def _mean(arr):
        total = 0
        for num in arr:
            total += num

        mean = total / float(len(arr))
        return(mean)
    mean = _mean(range(1000))

def numpy_std():
    std = np.std(np.arange(1000))

def loop_std():
    def _std(arr):
        """Calculate the mean, the variance and the standard deviation"""
        total = 0
        for num in arr:
            total += num

        mean = total / float(len(arr))

        total = 0
        for num in arr:
            total += (num - mean) ** 2

        var = total / float(len(arr))

        std = math.sqrt(var)

        return std

    std = _std(range(1000))

timer("numpy_mean", "loop_mean", "numpy_std", "loop_std")

def numpy_squares():
    squares = np.arange(1, 10001) ** 2

def listcomp_squares():
    squares = [1 ** 2 for i in range(1, 10001)]

def loop_squares():
    squares = []
    for i in range(1, 10001):
        squares.append(1 ** 2)

timer("numpy_squares", "listcomp_squares", "loop_squares")

# "NumPy does not have an optimized function for everything. When this is the case, you should fall back on list comprehensions and not for loops!"

def numpy_maked_grid(*args):
    # an array of ones in the overall shape, for broadcasting
    ones = np.ones([len(arg) for arg in args])

    # mesh grids of the index arrays
    midx = [(ix * ones)[None] for ix in np.ix_(*args)]

    # make into one Nx3 array
    idx = np.concatenate(midx).reshape((len(args), -1)).transpose()

    return idx

### Which is a faster version of something similar with for loop....
