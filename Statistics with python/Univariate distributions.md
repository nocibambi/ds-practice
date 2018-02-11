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

For the 95 % two-sided conﬁdence intervals, for example, you have to calculate the PPF(0.025) of the standard normal distribution to get the lower and upper limit of the conﬁdence interval.

### The Form of a Distribution
#### Location
#### Scale
#### Shape
### Probability density
## Discrete distributions
### Bernoulli distributions
### Binomial distributions
### Poisson distributions
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
