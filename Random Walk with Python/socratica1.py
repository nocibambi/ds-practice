import random

def random_walk(n):
    """A simple random walking simulator taking
    the number of movements and returning the distance taken"""
    x = 0
    y = 0

    for i in range(n):
        step = random.choice(['N', 'S', 'E', 'W'])
        if step == 'N':
            y = y + 1
        elif step == 'S':
            y = y - 1
        elif step == 'E':
            x = x + 1
        else:
            x = x - 1
    return(x, y)

dist = 0
avg_dist = 0
for i in range(25):
    walk = random_walk(10)
    dist = abs(walk[0]) + abs(walk[1])
    avg_dist += dist
    print(i, walk, "Distance from home = ", dist)

print("The average distance of 25 10-move long randow walks"
      "is:", avg_dist / 25)
