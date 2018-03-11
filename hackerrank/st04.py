# Test Case #2
# i1 = "30"
# i2 = "10 40 30 50 20 10 40 30 50 20 1 2 3 4 5 6 7 8 9 10 20 10 40 30 50 20 10 40 30 50"
# i3 = "1 2 3 4 5 6 7 8 9 10 1 2 3 4 5 6 7 8 9 10 10 40 30 50 20 10 40 30 50 20"

# Test case #5
i1 = "5"
i2 = "10 40 30 50 20"
i3 = "1 2 3 4 5"

size = int(i1)
numbers = list(map(int, i2.split()))
freqs = list(map(int, i3.split()))

# print(f"Numbers: {numbers}")
# print(f"Freqs: {freqs}")

def build(nums, freqs):
    array = []
    for i in range(size):
        for f in range(freqs[i]):
            array.append(nums[i])
    return array

array = sorted(build(numbers, freqs))
# print(f"Array: {array}")



def median(nums):
    hlen = len(nums) // 2
    if len(nums) % 2 == 1:
        med = nums[hlen]
        # print(med)
    else:
        # print("nums[hlen - 1 : hlen + 1]:" + str(nums[hlen - 1 : hlen + 1]))
        med = sum(nums[hlen - 1 : hlen + 1]) / 2
        # print(med)
    return med


def quartiles(nums):
    hsize = len(array) // 2
    # print(f"hsize: {hsize}")
    # qsize = hsize // 2

    first = nums[:hsize]

    if size % 2 == 1:
        # print("odd")
        # q2 = numbers[hsize] # Median
        second = nums[hsize + 1:]

    else:
        # print("even")
        # q2 = round((numbers[hsize] + numbers[hsize +1]) / 2)
        second = nums[hsize:]

    return first, second

first, second = quartiles(array)

q1 = median(first)
# q2 = median(numbers)
q3 = median(second)
range = float(round(q3 - q1, 1))


# print(f"Size: {size}")
# print("Length: " + str(len(numbers)))


# print(f"First: {first}")
# print(f"Second: {second}")
#
# print(q1)
# print(q2)
# print(q3)

# print(f"Range: {range}")
print(range)
