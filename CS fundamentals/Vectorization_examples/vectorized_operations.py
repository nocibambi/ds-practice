# Vectorizing the Haversine formula

## Original function
from numpy import sin, cos, pi, arcsin, sqrt
def get_distance(lat, lon, pcode_lat, pcode_lon):
    """
    Find the distance between `(lat,lon)` and the reference point
    `(pcode_lat,pcode_lon)`.
    """
    RAD_FACTOR = pi / 180.0  # degrees to radians for trig functions
    lat_in_rad = lat * RAD_FACTOR
    lon_in_rad = lon * RAD_FACTOR
    pcode_lat_in_rad = pcode_lat * RAD_FACTOR
    pcode_lon_in_rad = pcode_lon * RAD_FACTOR

    delta_lon = lon_in_rad - pcode_lon_in_rad
    delta_lat = lat_in_rad - pcode_lat_in_rad

    # Next two lines is the Haversine formula
    inverse_angle = (sin(delta_lat / 2) ** 2 + cos(pcode_lat_in_rad) *
                     cos(lat_in_rad) * sin(delta_lon / 2) ** 2)
    haversine_angle = 2 * arcsin(sqrt(inverse_angle))
    EARTH_RADIUS = 6367  # kilometers
    return haversine_angle * EARTH_RADIUS

# Random coordinates
from numpy import random
godatadriven = (52.3905927,4.8412508)

# First vectorization
points = random.randn(400000, 2) * 0.01
points[:, 0] = points[:, 0] + godatadriven[0]
points[:, 1] = points[:, 1] + godatadriven[1]
# "Scaling randn by 0.01 didn't require two for-loop for each of its elements: we simply told NumPy to multiply the whole array by 0.01 and it was done. The same when we added godatadriven[0] to points[:, 0]: we didn't have to write a for-loop for each element because once again NumPy took care of it."

# Measuring time
def iterate_distance():
    d = []
    for p in points:
        d.append(get_distance(p[0], p[1], godatadriven[0], godatadriven[1]))

import time

t1 = time.time()
iterate_distance()  # runs in 3.53 seconds
print("Running time of iterate_distance():\n{} us".format(1000000 * (time.time() - t1)))

# List comprehension
t1 = time.time()
[get_distance(p[0], p[1], godatadriven[0], godatadriven[1]) for p in points]
print("List comprehension time:\n{} us".format(1000000 * (time.time() - t1)))

# Vectorized
t1 = time.time()
get_distance(points[:, 0], points[:, 0], godatadriven[0], godatadriven[1])
print("Vectorized time:\n{} us".format(1000000 * (time.time() - t1)))
# We basically called the calculating function with the whole array on which it went through

# Further times and details: http://nbviewer.ipython.org/gist/gglanzani/9271842
