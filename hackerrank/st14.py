# Negative binomial experiment
#    * n repeated, independent trials
#    * outcomes are either success of failure
#    * P(s) is the same for every trial
#    * Experiment continues until x successes occur
# X: a discrete random variable, the number of experiments until the x^th success

# Negative binomial distribution
# b^*(x, n, p) = \binom{n - 1}{x - 1} \cdot p^x \cdot q^{n - x} = (n - 1)! / ((x - 1)!(n - x)!) \cdot p^x \cdot q^{n - x}
#   * x: number of observed successes
#   * n: number of trials
#   * p: probability of the success of 1 trial
#   * b^*(x, n, p): the negative binomial probability, that is, having x - 1 successes after n - 1 trials and having x successes after n trials

# Geometrical distribution
# A special case of the negative binomial distribution
# X: Number of Bernoulli trials to get a success
# X_i = \begin{cases} 1 &\text{if the } i^{th} &\text{trial is success} \\ 0 &\text{otherwise} \end{cases}

# Geometric distribution: negative distribution where the number of successes is 1.
# g(n, p) =  q^{n - 1} \cdot p

# Example: Bob is a high school basketball player. He is a 70% free throw shooter, meaning his probability of making a free throw is 0.70. What is the probability that Bob makes his first free throw on his fifth shot?

def geom_dist(n, p):
    return (1 - p) ** (n - 1) * p

bob_5th = round(geom_dist(5, 0.7), 5)
print(f"The probability of Bob making his first free throw on his fifth shot is: {bob_5th}")

# Task: The probability that a machine produces a defective product is 1/3. What is the probability that the 1st defect is found during the 5th inspection?

input1 = "1 3"
input2 = "5"

i1 = list(map(int, input1.split()))
i2 = int(input2)

p = i1[0] / i1[1]
n = i2

defect_5 = round(geom_dist(n, p), 3)
# The probability that the 1st defect is found during the 5th inspection
print(defect_5)
