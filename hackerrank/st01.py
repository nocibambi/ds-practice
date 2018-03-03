import pandas as pd

i1 = "10"
i2 = "64630 11735 14216 99233 14470 4978 73429 38120 51135 67060"

size = int(i1)
numbers = pd.Series(map(int, i2.split()))

print(numbers.mean())
print(numbers.median())
print(numbers.mode()[0])
