# A knight in standard international chess is sitting on a board as follows

# 0 1 2 3
# 4 5 6 7
# 8 9 10 11
# 12 13 14 15

# The knight starts on square "0" and makes jumps to other squares according to
# the allowable moves in Chess (so that at each space, it has between two to
# four valid moves). The knight chooses amongst the allowable moves at each jump
# uniformly at random and keeps track of the running sum of keys on which it
# lands. See below for specific questions and answers.

import numpy as np
import random

#steps = 16
#divisor = 13
#experiments = 1

universe = np.zeros((8,8), dtype=np.int8)

table = universe[2:-2,2:-2]
pos = (0,0)
table[pos] = 1


values = np.array(np.arange(16))
values.shape = (4, 4)
#modtab = table % divisor
#print(modtab)

moves = np.array([[ 1, 2],
                  [ 1,-2],
                  [ 2, 1],
                  [ 2,-1],
                  [-1, 2],
                  [-1,-2],
                  [-2, 1],
                  [-2,-1]])

cord = [2,1]
result = moves + cord

# Condition
(result >= [0,0]) & (result <= [3,3])

#posmoves = np.zeros((5,5))
posmoves = np.array([[0,1,0,1,0],
                     [1,0,0,0,1],
                     [0,0,0,0,0],
                     [1,0,0,0,1],
                     [0,1,0,1,0]])

# How to complement the posmoves matrix so it will be just as big
# as the universe so I can broadcast the two

self = (2,2) # The center point of the posmoves space

# Variation?
#posmoves = np.array([[0,0,0,0,0,0,0],
#                     [0,0,1,0,1,0,0],
#                     [0,1,0,0,0,1,0],
#                     [0,0,0,0,0,0,0],
#                     [0,1,0,0,0,1,0],
#                     [0,0,1,0,1,0,0],
#                     [0,0,0,0,0,0,0]])
#
#self = (4,4) # The center point of the posmoves space


space = np.ones((4,4))
jump = np.array([2,1])



cord = (2,1) # example move
# poss

[0,1]
[0,3]
[1,0]
[1,4]
[3,0]
[3,4]
[4,1]
[4,3]

# Condition after movement
condition = table == 1
value[condition]

coordinates = []
for i in range(table.shape[0]):
    for j in range(table.shape[1]):
        coordinates.append((i, j))

moves = [(2, 1), (2, -1),
         (-2, 1), (-2, -1),
         (1, 2), (1, -2),
         (-1, 2), (-1, -2)]

pos_moves = {}
for cor in coordinates:
    pos_moves[cor] = []
    for move in moves:
        if tuple(np.add(cor, move)) in coordinates:
            pos_moves[cor].append(move)

def knight(steps, divisor):
    cur_pos = (0, 0)
    pos_hist = []

    val = 0
    valhist = []
    cumval = 0
    cumvalhist = []

    mod = 0
    cummod = 0
    modhist = []

    for i in range(1, steps + 1):
        #print("startpoint: {}".format(cur_pos))

        move = random.choice(pos_moves[cur_pos])
        #print("move: {}".format(move))

        cur_pos = tuple(np.add(move, cur_pos))
        #print("cur_pos: {}".format(cur_pos))

        value = table[cur_pos[0], cur_pos[1]]
        #print("value: {}".format(value))

        cumval += value
        #print("cumval: {}".format(cumval))

        mod = cumval % divisor
        #print("mod: {}".format(mod))

        modhist.append(mod)
        #print("modhist: {}".format(modhist))

        #print("\n")

    avgmod = np.mean(modhist)
    #print("avgmod: {}".format(avgmod))

    stdmod = np.std(modhist)
    #print("stdmod: {}".format(stdmod))
    #print("\n")

    #print("avgmod (stdmod): {} ({})".format(avgmod, stdmod))
    return avgmod, stdmod, cumval


def simulations(steps, divisor, divquery, condition, experiments):
    avgs = []
    stds = []

    countcond = 0
    condtrues = []

    countdiv = 0
    divtrues = []
    divprob = 0

    for exp in range(experiments):
        #print(exp)
        avg, std, finval = knight(steps, divisor)
        avgs.append(avg)
        stds.append(std)

        if finval % condition == 0:
            countcond += 1
            condtrues.append(finval)
            if finval % divquery == 0:
                countdiv += 1
                divtrues.append(finval)

    if countcond == 0:
        pass
    else:
        divprob = countdiv / countcond

    print("Based on {} experiments, after {} steps the mean of the quantity S modulo {} is {} and the standard deviation is {}. For cases where the sum is divisible by {}, the probability of it being also divisible by {} is {}.".
    format(experiments, steps, divisor, np.mean(avgs), np.mean(stds), condition, divquery, divprob))

# After T = 16 moves, what is the mean of the quantity S modulo 13?
# What is the standard deviation?
# After T = 512 moves, what is the mean of the quantity S modulo 311?
# What is the standard deviation?
# After T = 16 moves, what is the probability that the sum is divisible by 5,
# given that it is divisible by 13?
# After T = 512 moves, what is the probability that the sum is divisible by 7,
# given that it is divisible by 43?

simulations(steps=16, divisor=13, divquery=5, condition=13, experiments=1000)
print("\n")
simulations(steps=512, divisor=311, divquery=7, condition=43, experiments=1000)
