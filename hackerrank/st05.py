input1 = "5"
input2 = "10 40 30 50 20"

from math import sqrt

i1 = int(input1)
i2 = list(map(int, input2.split()))

#size = int(i1)
#numbers = list(map(int, i2.split()))
#
## Calculating the mean
#mean = sum(numbers) / size
#
## Calculating distances
#distances = []
#for i in numbers:
#    distances.append((mean - i) ** 2)
#
## Calculating standard deviation
#st_dev = sqrt(sum(distances) / size)

i2 = numlist
mean = sum(numlist) / len(numlist)
variance = 0

for num in numlist:
    variance += (mean - num) ** 2

st_dev = sqrt(variance / len(numlist))

print(st_dev)
