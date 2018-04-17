# Solving with pandas

# import pandas as pd

input1 = "5"
input2 = "10 40 30 50 20"
input3 = "1 2 3 4 5"

i1 = int(input1)
i2 = list(map(int, input2.split()))
i3 = list(map(int, input3.split()))

# size = int(i1)
# numbers = pd.Series(map(int, i2.split()))
# weights = pd.Series(map(int, i3.split()))
#
# print((numbers * means).sum() / weights.sum())

# With the standard library

# Earlier solution
#size = int(input1)
#numbers = list(map(int, input2.split()))
#weights = list(map(int, input3.split()))
#
#total_sum = sum([n * w for n, w in zip(numbers, weights)])
#print(round(total_sum / sum(weights), 1))

totalsum = 0

for i in range(i1):
    totalsum += i2[i] * i3[i]

wmean = totalsum / sum(i3)

print(round(wmean, 1))
