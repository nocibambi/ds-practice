import random

def random_walk2(n):
    """Next step random walk function.
    Takes number of steps, returns coordinates"""
    x, y = 0, 0
    for i in range(n):
        # Here the two coordinates are defined together by
        # getting them as a tuple:
        (dx, dy) =  random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x, y)

walksum = 0

for i in range(25):
    walk = random_walk2(10)
    distance = abs(walk[0]) + abs(walk[1])
    walksum += distance
    print(walk, "Distance from home = ",
          abs(walk[0]) + abs(walk[1]))

print("The average distance taken during the 25 10-step walks:",
      walksum / 25)
