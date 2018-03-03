# Task: In a single toss of 2 fair (evenly-weighted) six-sided dice, find the probability that the values rolled by each die will be different and the two dice have a sum of 6.

dice = [1, 2, 3, 4, 5, 6]

rolls = []
for roll1 in dice:
    for roll2 in dice:
        tworoll = (roll1, roll2)
        rolls.append(tworoll) # List of dice toss combinations

f_dif6 = 0
for roll in rolls:
    if roll[0] != roll[1]:
        if sum(roll) == 6:
            f_dif6 += 1

p_dif6 = f_dif6 / len(rolls)

print(f"The probability of having two different values adding up to 6 is {f_dif6}/{len(rolls)} or {p_dif6}")
