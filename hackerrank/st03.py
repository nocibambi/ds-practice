# Solving with pandas
# import pandas as pd

input1 = "11"
input2 = "3 7 8 5 12 19 14 13 18 24 21"

i1 = int(input1)
i2 = list(map(int, input2.split()))
i3 = list(map(int, input3.split()))

# size = int(i1)
# numbers = pd.Series(map(int, i2.split()))
#
# q1 = numbers[:round(size / 2)]
# q3 = numbers[round(size / 2) + 1:]
#
# print(q1.median())
# print(numbers.median())
# print(q3.median())



size = int(i1)
numbers = sorted(list(map(int, i2.split())))

hsize = size // 2
# qsize = hsize // 2


def median(nums):
    hlen = len(nums) // 2
    if len(nums) % 2 == 1:
        med = nums[hlen]
        print(med)
    else:
        print("nums[hlen - 1 : hlen + 1]:" + str(nums[hlen - 1 : hlen + 1]))
        med = sum(nums[hlen - 1 : hlen + 1]) // 2
        print(med)
    return med

if size % 2 == 1:
    print("odd")
    # q2 = numbers[hsize] # Median

    first = numbers[:hsize]
    second = numbers[hsize + 1:]

else:
    print("even")
    # q2 = round((numbers[hsize] + numbers[hsize +1]) / 2)

    first = numbers[:hsize]
    second = numbers[hsize:]


q1 = median(first)
q2 = median(numbers)
q3 = median(second)

print(f"Size: {size}")
print("Length: " + str(len(numbers)))
print(f"Numbers: {numbers}")
print(f"First: {first}")
print(f"Second: {second}")

print(q1)
print(q2)
print(q3)
