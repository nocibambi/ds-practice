# Problem: when we cannot calculate $ p(x) $ with the usual f(n, x, p) formula we can use Poisson random variable.
#
# Poisson Experiment
#
# A Poisson experiment is a statistical experiment that has the following properties:
# * The outcome of each trial is either success or failure.
# * The average number of successes ($\lambda$) that occurs in a specified region is known.
# * The probability that a success will occur is proportional to the size of the region.
# * The probability that a success will occur in an extremely small region is virtually zero.

# Poisson random variable: The number of successes resulting from the poisson experiment
# Its probability distribution: $ P(k, \lambda) = \frac{\lambda^k e^{-\lambda}}{k!} $ where
# * $\lambda$: average number of successes in a specified region
# * $k$: actual number of successes in a specified region
# * $ P(k, \lambda)$: The probability of getting exactly $k$ successes when the average number of successes is $\lambda$

from math import e

def factor(num):
    fact = 1
    if num != 0:
        for i in range(1, num + 1):
            fact *= i
    return fact

def pois_dist(average_success, actual_success):
    prob_k_success = (average_success ** actual_success * e ** (-average_success)) / factor(actual_success)
    return prob_k_success

# Example 1
# Acme Realty company sells an average of 2 homes per day. What is the probability
# that exactly 3 homes will be sold tomorrow?
# avg_homes = 2
# exact_homes = 3
#
# prob_3_homes = pois_dist(2, 3)
# print(round(prob_3_homes, 3))

# Example 2
# Suppose the average number of lions seen by tourists on a one-day safari is 5.
# What is the probability that tourists will see fewer than 4 lions on the
# next one-day safari?
#
# avg_lion = 5
# max_lion = 3
#
# max_lion_prob = 0
#
# #print(pois_dist(5, 4))
#
# for lion in range(1, max_lion + 1):
#     max_lion_prob += pois_dist(avg_lion, lion)
#
# print(round(max_lion_prob, 4))
#
# If $E[X]$ is the expectation of $X$ which for Poisson distribution is
# $E[X] = \lambda$
# $E[X^2] = \lambda + \lambda ^ 2$

input1 = "2.5"
input2 = "5"

i1 = float(input1)
i2 = int(input2)

prob = pois_dist(i1, i2)
print(round(prob, 3))
