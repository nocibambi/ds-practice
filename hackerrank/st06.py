# Tutorial examples
# A dice throwing simulator
# import random
# result = 0
#
# for _ in range(2): # We throw the dice multiple times
#     result += random.choice(dice) # 'result' gives the sum of the roll results
#
# print(result)

# 1. Find the probability of getting an odd number when rolling a 6-sided fair die.
dice = [1, 2, 3, 4, 5, 6]
odd_sides = [1, 3, 5]

p_odd = len(odd_sides) / len(dice)
print(f"The probability of getting an odd number on a dice is: {p_odd}")

# 2. Find the probability of getting 1 head and 1 tail when 2 fair coins are tossed.
coin_sides = ("H", "T")

## Solving with itertools
# import itertools
# result = list(itertools.product(coin_sides, coin_sides))
# print(result)

coin_toss = []
for side1 in coin_sides:
    for side2 in coin_sides:
        toss = side1, side2
        coin_toss.append(toss)

different = []
for toss in coin_toss:
    if toss[0] == toss[1]:
        different.append(toss)

p_single = len(different) / len(coin_toss)

print(f"The probability of getting 1 head and 1 tail with 2 coin tosses: {p_single}")

# 3. Let A and B be two events such that P(A) = 2/5 and P(B) = 4/5. If the probability of the occurrence of either A or B is 3/5, find the probability of the occurrence of both A and B together (i.e., The intersection of A and B).
p_A = 2/5
p_B = 4/5

p_A_uni_B = 3/5

p_A_ins_B = p_A + p_B - p_A_uni_B
print(f"The probability of A and B occuring together is {p_A_ins_B}")

# Problem: In a single toss of 2 fair (evenly-weighted) six-sided dice, find the probability that their sum will be at most 9.

dice = [1, 2, 3, 4, 5, 6]

rolls = []
for roll1 in dice:
    for roll2 in dice:
        tworoll = (roll1, roll2)
        rolls.append(tworoll)

f_max9 = 0
for roll in rolls:
    value = sum(roll)
    if value <= 9:
        f_max9 += 1

p_max9 = f_max9 / len(rolls)

print(f"The probability of two dice having a value of at most 9 is {f_max9} / {len(rolls)} or {p_max9}")
