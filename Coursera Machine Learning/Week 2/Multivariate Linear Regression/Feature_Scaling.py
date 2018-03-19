# Values
ex1 = [89, 72, 94, 69]
ex2 = []
for i in ex1: ex2.append(i ** 2)
fex = [96, 74, 87, 78]


def feature_scale(list):
    range = max(list) - min(list)
    mean = sum(list) / len(list)
    norm = []

    for i in list:
        norm.append((i - mean) / range)

    return norm

n_ex1 = feature_scale(ex1)
print("The normalized feature x_i^(3) is : {}".format(round(n_ex1[2], 2)))
print("Haven't checked wheter it is correct!")
