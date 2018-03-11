# Permutations: when order matters
# The r-element permutation of an n-object set
# Orderly selecting r elements from an n size set
# p = n! / (n - r)!

# Combinations: when order does not matter
# Unordered selection of r elements from an n size set
# The possible combinations of r elements taken from n size set
# The number of r size subsets can be made of an n size set, 'n choose r'
# c = p / r! = n! / (r! * (n-r)!)

# You draw 2 cards from a standard 52-card deck without replacing them. What is the probability that both cards are of the same suit?
from fractions import Fraction

d = 2
A = 52
p0 = 13 / 52
p1 = 12 / 51

print(Fraction(p1).limit_denominator())
