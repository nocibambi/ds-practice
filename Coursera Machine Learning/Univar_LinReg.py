# Training examples
examples = [(3, 4), (2, 1), (4, 3), (0,1)]
m = len(examples)
omegas = (0, 1) # Linear regression hypothesis parameters

# Linear regression hypothesis
def linreg(x, os):
    """
    x: observed predictor
    os: the linear regression hypothesis parameters, given as a tuple
    """

    h0 = os[0] + os[1] * x
    return h0

# Cost function
def cost(tr_ex):
    """
    tr_ex: the training examples as a list of tuples
    """
    sum = 0

    for x, y in tr_ex:
        sum += (linreg(x, omegas) - y) ** 2
        print(f"sum: {sum}")

    cost = 1/(2 * m) * sum
    return cost

print(cost(examples))
print(f"linreg(6, (-1, 2)): {linreg(6, (-1, 2))}")
