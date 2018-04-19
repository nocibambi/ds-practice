# A bag contains 3 red marbles and 4 blue marbles.
# Then, 2 marbles are drawn from the bag, at random, without replacement.
# If the first marble drawn is red, what is the probability that the second
# marble is blue?

from fractions import Fraction

r0 = 3
r1 = 2
b = 4

p = b / (r1 + b)
print(Fraction(p).limit_denominator())
