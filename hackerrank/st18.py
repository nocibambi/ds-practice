# Normal Distribution
# The probability density of normal distribution is:
# ```math
# N(\mu, sigma^2) =
#  frac{1}{\sigma \sqrt{2 \pi}}
#   \e ^ {- \frac{(x-\mu)^2}{2\sigma^2}}
# ```
# Here,
#
# * $\mu$ is the mean (or expectation) of the distribution. It is also equal to median and mode of the distribution.
# * $\sigma^2$ is the variance.
# * $\sigma$  is the standard deviation.
#
# Standard Normal Distribution
#
# If $\mu = 0$ and $\sigma = 1$, then the normal distribution is known as
# standard normal distribution:
#
# ```math
# \Phi(x) = \frac{e^{-frac{x^2}{2}}}{\sqrt{2 \pi}}
# ```
#
# Every normal distribution can be represented as standard normal distribution.
#
# Cumulative Probability
#
# Consider a real-valued random variable, X.
# The cumulative distribution function of X (or just the distribution function
# of X) evaluated at x is the probability that will take a value less than or
# equal to x.
#
# The cumulative distribution function for a function with normal distribution is:
#
# ```math
# \Phi(x) = frac{1}{2} (1 + erf(\frac{x - \mu}{\sigma \sqrt{2}}))
# ```
#
# Where is the error function:
# ```math
# erf(z) = \frac{2}{\sqrt{\pi}} \integral_{0}^{z} e^{-x^2}dx
# ```

# Task
# In a certain plant, the time taken to assemble a car is a random variable, X,
# having a normal distribution with a mean of 20 hours and a standard deviation
# of 2 hours. What is the probability that a car can be assembled at this plant in:
# * Less than 19.5 hours?
# * Between 20 and 22 hours?


input1 = "20 2"
input2 = "19.5"
input3 = "20 22"

i1 = list(map(int, input1.split()))
i2 = float(input2)
i3 = list(map(int, input3.split()))

from math import pi, e, sqrt

def err_func(z, x):
    err = 2/sqrt(pi) * integral(0, z, x, e ** (-x ** 2))
    return err

def cumdist_func(x, mean, std):
    prob = 1/2 * (1 + err_func((x - mean) / (std * sqrt(2))))
    return prob

mean = i1[0]
std = i1[1]
x1 = i2

x2_min = i3[0]
x2_max = i3[1]

prob1 =
