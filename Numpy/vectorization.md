# things to check:
- [ ] printing timeit results from a file.

# Pandas
* https://campus.datacamp.com/courses/manipulating-dataframes-with-pandas/extracting-and-transforming-data?ex=16#skiponboarding
* https://www.datascience.com/blog/straightening-loops-how-to-vectorize-data-aggregation-with-pandas-and-numpy/
* https://jakevdp.github.io/PythonDataScienceHandbook/03.12-performance-eval-and-query.html
* https://tomaugspurger.github.io/modern-4-performance
* https://www.youtube.com/watch?v=hvSEZxcH9PM
* https://www.lynda.com/Pandas-tutorials/Vectorized-operations/518161/551099-4.html
* https://www.youtube.com/results?search_query=vectorization+python

# Numpy tutorials
* https://www.datacamp.com/community/tutorials/python-numpy-tutorial
* https://www.dataquest.io/blog/numpy-tutorial-python/
* https://jakevdp.github.io/PythonDataScienceHandbook/02.00-introduction-to-numpy.html
* http://mail.scipy.org/mailman/listinfo/numpy-discussion
* Reviewed:
  * https://www.labri.fr/perso/nrougier/teaching/numpy/numpy.html

# Vectorized solutions
* https://softwareengineering.stackexchange.com/questions/254475/how-do-i-move-away-from-the-for-loop-school-of-thought
* https://stackoverflow.com/questions/17792077/vectorizing-for-loops-numpy
* http://stupidpythonideas.blogspot.hu/2015/09/going-faster-with-numpy.html
* http://www.jesshamrick.com/2012/04/29/the-demise-of-for-loops/
* https://hackernoon.com/speeding-up-your-code-2-vectorizing-the-loops-with-numpy-e380e939bed3
* https://datascience.blog.wzb.eu/2018/02/02/vectorization-and-parallelization-in-python-with-numpy-and-pandas/
* https://engineering.upside.com/a-beginners-guide-to-optimizing-pandas-code-for-speed-c09ef2c6a4d6
* https://stackoverflow.com/questions/46959044/how-to-calculate-the-probability-mass-function-of-a-random-variable-modulo-n-wh
* https://www.youtube.com/watch?v=gVgFblfuEW8
* http://faculty.washington.edu/rjl/uwamath583s11/sphinx/notes/html/python_vect.html
* https://ep2015.europython.eu/media/conference/slides/numpy-vectorize-your-brain.pdf
* https://blog.godatadriven.com/the-performance-impact-of-vectorized-operations.html
* https://stackoverflow.com/questions/27575854/vectorizing-a-function-in-pandas
* https://stackoverflow.com/questions/48777345/vectorized-random-walk-in-python-with-boundaries

# Memoization
https://www.youtube.com/watch?v=Qk0zUZW-U_M
https://www.python-course.eu/python3_memoization.php

# Data science python performance
* http://dataconomy.com/2017/07/big-data-numpy-numba-python/
* http://machinelearningexp.com/data-science-performance-of-python-vs-pandas-vs-numpy/
* http://know.continuum.io/rs/387-XNW-688/images/Whitepaper_HiPerfForODS_V9_small.pdf

# Read
* https://towardsdatascience.com/why-you-should-forget-for-loop-for-data-science-code-and-embrace-vectorization-696632622d5f
* https://towardsdatascience.com/data-science-with-python-turn-your-conditional-loops-to-numpy-vectors-9484ff9c622e

# Examples
From https://softwareengineering.stackexchange.com/questions/254475/how-do-i-move-away-from-the-for-loop-school-of-thought

# Problem 1
```py
def sumproducts(x, y):
    """Return the sum of x[i] * y[j] for all pairs of indices i, j.

    >>> sumproducts(np.arange(3000), np.arange(3000))
    20236502250000

    """
    result = 0
    for i in range(len(x)):
        for j in range(len(y)):
            result += x[i] * y[j]
    return result
```

## Solution
```py

```
