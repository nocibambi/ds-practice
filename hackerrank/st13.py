# A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of 10 pistons will contain:
# 1. No more than 2 rejects?
# 2. At least 2 rejects?

from math import factorial
def bin_dist(x, n, p):
    n_choose_x = factorial(n) / (factorial(x) * factorial(n - x))
    bin_prob =  n_choose_x * p ** x * (1 - p) ** (n - x)
    return bin_prob

input = "12 10"

i = list(map(float, input().split()))
p = i[0] / 100
n = i[1]

# No more than 2 rejects
max2 = round(sum(bin_dist(x, n, p) for x in range(3)), 3)
# The probability of having no more than 2 rejects from a batch of 10 pistons
print(max2)

# At least 2 rejects
min2 = round(sum(bin_dist(x, n, p) for x in range(2, 11)), 3)
# The probability of having at least 2 rejects from a batch of 10 pistons
print(min2)
