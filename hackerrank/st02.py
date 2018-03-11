# Solving with pandas

# import pandas as pd

i1 = "5"
i2 = "10 40 30 50 20"
i3 = "1 2 3 4 5"

# size = int(i1)
# numbers = pd.Series(map(int, i2.split()))
# weights = pd.Series(map(int, i3.split()))
#
# print((numbers * means).sum() / weights.sum())

# With the standard library
size = int(i1)
numbers = list(map(int, i2.split()))
weights = list(map(int, i3.split()))

total_sum = sum([n * w for n, w in zip(numbers, weights)])
print(round(total_sum / sum(weights), 1))
