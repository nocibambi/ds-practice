# Univariate distributions

## Characteristics of distributions
### Distribution center
Two ways to evaluate data:
1. By value
2. By rank (list-number in an order of magnitude)

#### Mean
```math
\bar{x} = \frac {\sum_{i = 1}^{n} x_i} {n}
```
```python
import numpy as np
np.mean()
```

#### Median
The value that comes half-way when the data are ranked in order.
```python
import pandas as pd
pd.median()
```

#### Mode
The most frequently occurring value in a distribution.
```python
from scipy import stats
stats.mode()
```

#### Geometric mean
It can be useful to describe the location of a distribution.
```math
mean_{geometric} = (\prod_{i=1}^{N} X_i) ^ {1/N} = exp (\frac{\sum_{i}  ln{x_i}}n)
```
```python
from scipy import stats
stats.gmean()
```
> Its output numbers have to be positive

### Quantifying variability
#### Range
'Peak-to-peak' distance. Need to look out for outliers.

```python
import numpy as np
range = np.ptp(x)
```

#### Percentiles
##### Cumulative distribution function (CDF)
```math
CDF(x) = \int_{\infty}^{x} PDF(x)dx
```
##### Probability between a and b
The probability to ﬁnd a value between a and b is given by the integral over the PDF in that range, and can be found by the difference of the corresponding CDF-values:
```math
P(a \le X \le b) = \int_{a}^{b} PDF(x)dx = CDF(b) - CDF(a)
```
For discrete distributions, the integral has to be replaced by a sum.
##### Percentiles
The inverse of the CDF, and give the value below which a given percentage of the data values occur.

#### Standard deviation and Variance
Two types:
##### Sample variance
In refers to the sampled data. The maximum likelihood estimator of the sample variance:
```math
var = \frac{\sum_{1}^{n} (x_i - \bar{x}) ^2} {n}
```
But it is a 'biased estimator' of the population variance because it systematically undervalues it.

##### Population variance
In refers to the full population. The best unbiased estimator of the population variance:
```math
var = \frac {\sum_{1}^{n} (x_i - \bar{x}) ^2} {n - 1}
```

##### Standard deviance
* Standard deviation: Square root of the variance
* Sample standard deviation: square root of the sample variance
```math
s = \sqrt{var}
```

In numpy the default deviation is the standard. For the sample standard, the degree of freedom (ddof) needs to be '1'. In pandas the ddof is '1' by default.
```python
data = np.arange(7, 14)
np.std(data, ddof = 0) # Standard deviation
np.std(data, ddof = 1) # Sample standard deviation
```

#### Standard error
The standard error is the estimate of the standard deviation of a coefﬁcient.

For _normally_ distributed data, the **sample standard error of the mean** is
```math
SEM = \frac{s}{\sqrt{n}} = \sqrt {\frac {\sum_{i = 1}^{n} (x_i - \bar{x}) ^2} {n - 1}} \cdot \frac{1} {\sqrt{n}}
```

#### Confidence intervals
The $\alpha$% conﬁdence interval (CI) reports the range that contains
the true value for the parameter with a likelihood of $\alpha$%.

If the sampling distribution is symmetrical and unimodal, an approximation of the confidence interval is
```math
ci = mean \pm std * N_{PPF}(\frac{1 - \alpha}{2})
```
where $N_{PPF}$ the percentile point function (PPF) for the standard normal distribution.
* To calculate the conﬁdence interval **for the mean** value, the standard deviation has to be replaced by the standard error.
* If the distribution is **skewed**, is not appropriate and does not provide the correct conﬁdence intervals!

"For the 95 % two-sided conﬁdence intervals, for example, you have to calculate the PPF(0.025) of the standard normal distribution to get the lower and upper limit of the conﬁdence interval."

### The Form of a Distribution
Continuous distribution functions are characterized by their location and scale. Examples:
* Normal distribution: mean and standard deviation.
* Uniform distribution: start and end of the 'non-zero' range.

#### Location
$x_0$  location parameter:
```math
f_{x0}(x) = f(x - x_0)
```
Examples:
* Mean
* Median
* Mode

#### Scale
$s$ width of the distribution:
```math
f_s(x) = f(x/s)/s
```
Where $f$ is the density of a standardized version of the density.[???]

#### Shape
Parameters beyond location and scale.

##### Skewness
A depart from symmetry
* Positive skewness: when the standard deviation is more than half the mean
* Negative skewness is its opposite

##### Kurtosis
Measure of 'peakedness'
* Normal distribution: kurtosis of 3
* Excess kurtosis: $ kurtosis - 3 $ (0 for the normal distribution)
    - Negative excess kurtosis: platykurtic distribution
    - Positive excess kurtosis: leptokurtic distribution

### Presentations of probability density
* Probability density function (PDF)
* Cumulative distribution function (CDF): the probability of getting a value smaller than a given threshold
* Survival Function (SF): its opposite, 1 - CDF, the proportion of data 'surviving' above a certain value
* Percentile Point Function (PPF): the input value of the CDF with a given probability value (the inverse of the CDF)
* Inverse Survival Function (ISF)
* Random Variate Sample (RVS): random variates of a given distribution

```python
import numpy as np
from scipy import stats

myDF = stats.norms(5,3) # 1. step: creating a 'frozen' distribution (i.e. it is not a function yet!)

x = np.linspace(-5, 15, 101)
y = myDF.cdf(x) # 2. step: Choosing a function and calculating its value for the distribution.
```

## Discrete distributions
The two main types:
* Binomial: have a maximum limit (e.g. result of five dice rolls)
* Poission: unlimited (number of people to know)

### Bernoulli distributions
It has only two states.
* The most simple univariate distribution, and the basis of the binomial.

```math
P_{1} + P_{2} = 1
```

```python
from scipy import stats
p = 0.5
bern_dist = stats.bernoulli(p) # This is a 'frozen distribution function'

p_tails = bern_dist.pmf(0) # Probability of zero heads
p_heads = bern_dist.pmf(1) # Probability of one head

# Simulating 10 trials
trials = bern_dist.rvs(10) # 'rvs' stands for random variates

# Gives the outcomes of the trials
# array([0, 0, 1, 0, 1, 0, 0, 1, 0, 0])
```

### Binomial distributions
"How many trials will succeed from a given number?"
* e.g. how many people in a room have green eyes?

* X: number of successes
* $ X \in B(n, p) $

```math
P[X = k] = p^k (1 - p)^{n - k} \qquad 0 \le p \le, \qquad n \in N
```

```python
from scipy import stats
import numpy as np

(p, num) = (0.5, 4)
binom_dist = stats.binom(num, p) # Creating the frozen distribution function

binom_dist.pmf(np.arange(6))

# Returns the probability of each outcomes
# array([0.0625, 0.25  , 0.375 , 0.25  , 0.0625, 0.    ])
# e.g. the probability of zero successes is 0.0625
# e.g. the probability of exactly 1 success is 0.25
# e.g. the probability of exactly 5 successes is 0
# These all add up to one.

# Binomial test
check_val
# One-sided test: the likelihood of getting the same or more 'successes'
one_tail = binom_dist.sf(check_val-1)

# Two-sided test: the number of cases 'as extreme or more' than the given case are likely to occur
two_tail = binom_dist.sf(check_val, n, p)
```

### Poisson distributions
Examines the number of times an event might happen over a continuous period.
* There is no total value of 'n'-s.
* $ \lambda $: the 'average or expected' number of events happening
* The random variable X can take an nonnegative integer value
* eg.
  - How many pennies I find on my walk home?
  - How many defects will there be per 100 m of rope sold?

```math
P(X = k) = \frac {e^{-\lambda} \lambda^k} {k!}
```

### Normal distributions

### Central Limit Theorem
### Distribution and hypothesis test
## Continuous distributions derived from the normal distribution
### t-distribution
### Chi-Square distribution
### F-Distribution
### Other continuous distribution
### Lognormal distribution
### Weibull distribution
### Exponential distribution
### Uniform distribution
