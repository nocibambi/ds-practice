# Examples and exercises from http://www.labri.fr/perso/nrougier/from-python-to-numpy
# Errors:
    # compute_neighbors does not pass shape value to the iterate function
    # timeit does not work (cannot import tools)

# Random walk examples

## Object oriented approach
import numpy as np
import random

class RandomWalker:
    def __init__(self):
        self.position = 0

    def walk(self, n):
        self.position = 0
        for i in range(n):
            yield self.position
            self.position += 2*random.randint(0,1) - 1

walker = RandomWalker()
walk = [position for position in walker.walk(1000)]

from timeit import timeit
#timeit("[position for position in walker.walk(n=10000)]", globals()) #, globals()

# Procedural approach
def random_walk(n):
    position = 0
    walk = [position]
    for i in range(n):
        position += 2 * random.randint(0, 1) -1
        walk.append(position)
    return walk

#walk = random_walk(1000)
#timeit("random_walk(n=10000)", globals()) # some time saving, but not too much

# Vectorized approach
# First we use `itertools` for creating iterators for efficient looping. This vectorizes the function by
# 1. generate all the steps at once
# 2. with `accumulate` we calculate all the positions

def random_walk_faster(n=1000):
    from itertools import accumulate
    steps = random.choices([-1, +1], k=n)
    return [0]+list(accumulate(steps))

#walk = random_walk_faster(1000)

#timeit("random_walk_faster(n=1000)", globals())

# Vectorization with NumPy
def rand_walk_fastest(n=1000):
    # No 's' in NumPy choice (Python offers choice & choices)
    steps = np.random.choice([-1,+1], n)
    return np.cumsum(steps)

#walk = rand_walk_fastest(1000)
#timeit("random_walk_fastest(n=1000)", globals())

# The numpy array
## How to clear the values of an array as fast as poosible?
Z = np.ones(4*1000000, np.float32)
Z[...] = 0

# Compatible datatypes:
# Z.size * Z.itemsize can be divided by the new dtype itemsize
