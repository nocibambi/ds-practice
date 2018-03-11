# Conditional probability
# p_b|a: probability of b while a has already occured
# Independent (they have no effect on each other)
# p_b|a = p_b

# Non-independent:
# p_b|a = (p_a * p_b) / p_a

# Bayes theorem
# p_a|b = (p_b|a * p_a) / p_b =
# = (p_b|a * p_a) / (p_b|a * p_a * p_b|a' * p_a')

# 1. If the probability of student A passing an exam is 2/7 and the probability of student B failing the exam is 3/7, then find the probability that at least 1 of the 2 students will pass the exam.
from fractions import Fraction

p_a = 2/7
p_b = 4/7

# a and b are independent: p(a & b) = p_a * p_b
# p(a | b) = p_a + p_b - p(a & b) = p_a + p (b) - p_a * p_b

x1 = p_a + p_b - p_a * p_b
x2 = 1 - (1 - p_a) * (1 - p_b)
print(Fraction(x1).limit_denominator())
print(Fraction(x2).limit_denominator())

# 2. Historical data shows that it has only rained 5 days per year in some desert region (assuming a 365 day year). A meteorologist predicts that it will rain today. When it actually rains, the meteorologist correctly predicts rain 90% of the time. When it doesn't rain, the meteorologist incorrectly predicts rain 10% of the time. Find the probability that it will rain today.

r = 5 / 365 # Probability of raining today
r_ = 360 / 365 # Probability of not raining today
# m: Prediction of raining today
mr = 9 / 10 # Correct predictions of rain on rainy days, probability of prediction on rainy days
mr_ = 1 / 10 # Inorrect predictions on non-rainy days, probability of prediction on non-rainy days
# q = rm, probability of rain when there is a prediction for it

rm = (mr * r) / (mr * r + mr_ * r_)
print(Fraction(rm).limit_denominator())

# Suppose a family has 2 children, one of which is a boy. What is the probability that both children are boys?
p = 1 / 2
# q: the probability of a second boy, if the first is already a boy
# q = p(b2|b1)

print("lol")
