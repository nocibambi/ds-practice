# Given two numbers A and B and we generate x and y using the random number generator with uniform probability density function [0, A] and [0, B] respectively, what's the probability that x + y is less than C? where C is a positive integer.

from fractions import Fraction

N = int("3")
# N = int(input())
i1 = "1 1 1"
i2 = "1 1 2"
i3 = "1 1 3"

n1 = list(map(int, i1.split()))
n2 = list(map(int, i2.split()))
n3 = list(map(int, i3.split()))

# ranges
# 0-1 + 0-1 = 0-2
# 0-2 - 0-1 = 0-1


# def p_max(n):
#     if sum(n[:2]) <= n[2]:
#         p = 1
#     else:
#         p = (sum(n[:2]) - n[2]) / sum(n[:2])
#     return p

p1 = (sum(n1[:2]) - n1[2]) / sum(n1[:2])
p2 = (sum(n2[:2]) - n2[2]) / sum(n2[:2])
p3 = (sum(n3[:2]) - n3[2]) / sum(n3[:2])

# print(Fraction(p1))
# print(Fraction(p2))
# print(Fraction(p3))

# for i in range(N):
#     n = list(map(int, input().split()))
#     print(Fraction(p_max(n), denominator = 1))

print(Fraction(p_max(p1)))
print(Fraction(p_max(p2)))
print(Fraction(p_max(p3)))
