# A manufacturer of metal pistons finds that, on average, 12% of the pistons
# they manufacture are rejected because they are incorrectly sized.
# What is the probability that a batch of 10 pistons will contain:
# 1. No more than 2 rejects?
# 2. At least 2 rejects?

input1 = "12 10"

#from math import factorial
#def bin_dist(x, n, p):
#    n_choose_x = factorial(n) / (factorial(x) * factorial(n - x))
#    bin_prob =  n_choose_x * p ** x * (1 - p) ** (n - x)
#    return bin_prob
#
#
#i = list(map(float, input.split()))
#p = i[0] / 100
#n = i[1]
#
## No more than 2 rejects
#max2 = round(sum(bin_dist(x, n, p) for x in range(3)), 3)
## The probability of having no more than 2 rejects from a batch of 10 pistons
#print(max2)
#
## At least 2 rejects
#min2 = round(sum(bin_dist(x, n, p) for x in range(2, 11)), 3)
## The probability of having at least 2 rejects from a batch of 10 pistons
#print(min2)

# Results
#0.891
#0.342


def factor(num):
    fact = 1
    if num != 0:
        for i in range(1, num + 1):
            fact *= i
    return fact

def nchoosex(trials, successes):
    nundx = factor(trials) / (factor(successes) * factor(trials - successes))
    return nundx

def bindist(prob, tri, suc):
    dist = nchoosex(tri, suc) * prob ** suc * (1 - prob) ** (tri - suc)
    return dist

inp = list(map(int, input1.split()))

prob_reject = inp[0] / 100
batch = inp[1]
success = 2

max2rej = 0

for i in range(success + 1):
    max2rej += bindist(prob_reject, batch, i)

min2rej = 0
for i in range(success, batch + 1):
    min2rej += bindist(prob_reject, batch, i)


print(round(max2rej, 3))
print(round(min2rej, 3))
