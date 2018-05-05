# Numpy and pandas
* `df1._data` allows to see the datablocks stored for that particular dataframe
* any textual data column has the 'object' datatype and therefore is not effective to use

# Pandas and postresql
* pandas is always faster sometimes 5-10 times
* pandas stores the data in the memory which however can be a constraining factor very fast as the data grows

# Pandas and excel
## Filtering:
1. creating a boolean index for the conditions
2. applying the indices on the original dataset

in code:
```py
IX = sections['Section'] == 'A'  # Boolean (True/False) indices or rows that met our filtering criteria
sections[IX]  # use the Boolean indices to access rows
```

## Pivot table/aggregated values
```py
student_data.groupby('Section').agg({'Exam 1 Score':['max', 'mean'], 'Exam 2 Score': ['max', 'min']})
```
# Scikit-learn vs statsmodel
* scikit-learn is more easy to use, but hides most of the stats behind the models
* for more serious stat analysis we might want to use statsmodels

# Vectorization
Calculating dot product with numpy.
```py
import numpy as np

x = np.random.randn(1000000)
y = np.random.randn(1000000)

%timeit sum(x[i] * y[i] for i in range(len(x)))
%timeit np.dot(x, y)
```

Related topics:
* BLAS
* LABPACK
* dot product
* vectorized linear algebra
* numpy
* scipy
* timeit: https://stackoverflow.com/a/24105845/7648578

# Simulation
Trying to answer the following bernoulli distribution problem:
"You flip a fair coin n times.  What is the expected number of heads?  What is the standard deviation of the number of heads?"


```py
np.random.seed(123)
samples = np.random.randint(0, 2, 10000)
samples.mean()
samples.std()
```
Further, related topics:
* Dynamical Systems
* Monte Carlo
* Gibbs Sampling
* Importance Sampling
* MCMC
* bootstrapping

# Recursion

```py
def fib(n):
  if n < 2:
    return 1
  else:
    return fib(n - 1) + fib(n - 2)

%timeit fib(32)
```
Solving the coin flipping problem with recursion
```py
def average_heads(n):
  if n == 1:
    return 0.5
  else:
    return np.mean([average_heads(n-1) + 1./n, average_heads(n-1) - 1./n])
%timeit average_heads(10)
```
How to calculate variance with the same method?

Problem: How many possible ways (including drawing order) are there to draw US coins that sum up to 50 cents?
```py
coins = [1, 5, 10, 25, 50]
def count(remainder):
  if remainder < 0:
    return 0
  if remainder == 0:
    return 1
  # Calculates the number
  return sum(count(remainder - coin) for coin in coins)
count(50)
```
Further related topics:
* Depth-First Search
* Breadth-First Search
* Tail recursion

# Memoization and dynamic programming
It is inefficient to call the recursive function multiple times for the same input. We can 'remember' or memoize the results of previous computations.

There is a specific python decorator for this.

```py
@memoized # This turns the recursive program into a dynamically programmed one
def fib(n):
  if n < 2:
    return 1
  else:
    return fib(n - 1) + fib(n - 2)

%timeit fib(32)
```

# Breaking up problems
An example is solving the fibonacci sequence in a matrix form.
```py
M = np.matrix([[1, 1], [1, 0]])

def fib(n):
    if n < 2:
      return 1
    MProd = M.copy()

    for _ in range(n-2):
      MProd *= M

    return MProd[0,0] + MProd[0,1]

%timeit fib(32)
```
