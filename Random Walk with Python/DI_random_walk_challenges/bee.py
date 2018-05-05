# A bee walks around on a honeycomb, an infinite tessalating hexagonal grid,
# starting at a fixed hexagon. At each step, the bee moves to one of the six adjacent
# hexagons with equal probability. We'll assume adjacent hexagons are always a
# distance of one unit away from each other.

# directions = [N, NE, SE, S, SW, NW]

import random
import numpy as np
import pandas as pd

def bee(steps):
    distance = 0
    change = 0

    for step in range(1, steps + 1):
        #print("step: {}".format(step))
        if distance == 0: # Movement from the starting point
            change = 1
        else: # Steps outside the starting point
            change = random.choices([-1, 0, 1], [1/6, 2/6, 3/6])[0]
        #print("change: {}".format(change))
        distance += change
        #print("distance: {}".format(distance))
        #print("\n")
    return distance


def simulation(steps, experiments, distquery, mincond):
    distances = []
    expdist = 0
    expdev = 0


    for exp in range(experiments):
        distances.append(bee(steps))
    expdist = np.mean(distances)
    devs = abs(expdist - distances)
    expdev = np.mean(devs)

    condtrues = 0
    querytrues = 0
    for distance in distances:
        if distance >= mincond:
            condtrues += 1
            if distance >= distquery:
                querytrues += 1

    if condtrues != 0:
        probquery = querytrues / condtrues

    print("Based on {} experiments, after {} steps, the expected value of the bee's distance from the starting point is {} with {} expected deviation. The probability that its distance is at least {}, given that it is at least {}, is {}."
    .format(experiments, steps, expdist, expdev, distquery, mincond, probquery))

# After 16 steps, what is the expected value of the bee's distance from the starting hexagon?
# After 16 steps, what is the expected value of the deviation of the bee's distance from the starting hexagon?

# After 64 steps, what is the expected value of the bee's distance from the starting hexagon?
# After 64 steps, what is the expected value of the deviation of the bee's distance from the starting hexagon?

simulation(16, 1000000, 8, 6)
print("\n")
simulation(64, 1000000, 24, 20)

# After 16 moves, what is the probability that the bee is at least A = 8 distance away from the starting hexagon, given it is at least B = 6 distance?
# After 16 moves, what is the probability that the bee is at least A = 24 distance away from the starting hexagon, given it is at least B = 20 distance?
