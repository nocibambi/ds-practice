# Random variable
# A set of probabilities for the possible outcomes of a sample space.

# Binomial experiment: a statistical experiment with the following properties:
# n repeated independent trials
# the outcomes are binary (e.g. success or failure)

# Bernoulli random variable
# sample space have only two points
# f(x) =  p^x (1 - p)^{1-x}, \quad \text{for} \quad  x \in \{0, 1\}

# Binomial distribution
# n: number of trials
# x: number of successes
# p: probability of 'success' of one trial
# q: prob of a 'failure' trial
# b(x, n, p): binomial probability: having exactly x successes out of n trials
# binomial random variable: number of successes, x, out of n trials
# binomial distribution: b(x, n, p) = n! / (x! (n - x)!) * p^x * q^{n-x}

#from math import factorial
#
#def bin_dist(x, n, p):
#    n_choose_x = factorial(n) / (factorial(x) * factorial(n - x))
#    bin_prob =  n_choose_x * p ** x * (1 - p) ** (n - x)
#    return bin_prob


# Cumulative probability
# F_x(x) = P(X <= x)
# Cumulative distribution function (CDF): Non-decreasing function that
# accumulate all the probabilities for the values of X up to (and including) x
# P(a < X <= b) = F_x(b) - F_x(a)

# Fair coin is tossed 10 times. What are the probabilities of
# Getting 5 heads
# Getting at least 5 heads
# Getting at most 5 heads

#n = 10
#p = 0.5
#q = 0.5

# Getting 5 heads
# binomial probability: having exactly 5 successes
#x = 5
#print("The probability of having exactly 5 heads in 10 tosses.")
#print(bin_dist(x, n, p))
#
## Getting at least 5 heads
#print("The probability of having at least 5 heads in 10 tosses.")
#print(sum(bin_dist(i, n, p) for i in range(5,11)))
#
## Getting at most 5 heads
#print("The probability of having at most 5 heads in 10 tosses.")
#print(sum(bin_dist(i, n, p) for i in range(0,6)))
#print("\n")

# Task: The ratio of boys to girls for babies born in Russia is 1.09:1.
# If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?

# Write a program to compute the answer using the above parameters.
# Then print your result, rounded to a scale of 3 decimal places (i.e., 1.234 format).

input = "1.09 1"
#births = 6
#boys = 3
#
#ratio = list(map(float, input.split()))
#prob_boys = ratio[0] / sum(ratio)
#
#prob3_6 = sum(bin_dist(i, births, prob_boys) for i in range(3, 7))

# The probability of having at least 3 boys
#print(round(prob3_6, 3))

def factor(num):
    fact = 1
    if num != 0:
        for i in range(1, num + 1):
            fact *= i
    return fact

def nchoosex(trials, successes):
    nundx = factor(trials) / (factor(successes) * factor(trials - successes))
    return nundx

def bernoulli(prob, trials):
    dist = prob ** trials * (1 - prob) ** (1 - trials)

def bindist(prob, tri, suc):
    dist = nchoosex(tri, suc) * prob ** suc * (1 - prob) ** (tri - suc)
    return dist

odds = list(map(float, input.split()))
prob_boys = odds[0] / sum(odds)

trials = 6
successes = 3

sumprob = 0
for i in range(3, 6 + 1):
    sumprob += bindist(prob_boys, trials, i)

print(round(sumprob, 3))
