from math import sqrt

i1 = "5"
i2 = "10 40 30 50 20"

size = int(i1)
numbers = list(map(int, i2.split()))

# Calculating the mean
mean = sum(numbers) / size

# Calculating distances
distances = []
for i in numbers:
    distances.append((mean - i) ** 2)

# Calculating standard deviation
st_dev = sqrt(sum(distances) / size)

print(st_dev)
