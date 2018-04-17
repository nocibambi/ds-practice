# In this challenge, we go further with geometric distributions. We recommend
# reviewing the Geometric Distribution tutorial before attempting this challenge.

# Task
# The probability that a machine produces a defective product is 1/3.
# What is the probability that the 1st defect is found during the first
# 5 inspections?


input1 = "1 3"
input2 = "5"

i1 = list(map(int, input1.split()))
i2 = int(input2)

p = i1[0] / i1[1]
n = i2

def geom_dist(prob, trial):
    dist = (1 - prob) ** (trial - 1) * prob
    return dist

#di5 = geom_dist(p, n)
di5 = 0

for i in range(1, n + 1):
    di5 += geom_dist(p, i)

print(round(di5, 3))
