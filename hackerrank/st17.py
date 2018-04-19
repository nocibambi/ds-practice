input1 = "0.88 1.55"

i1 = list(map(float, input1.split()))


from math import e

def factor(num):
    fact = 1
    if num != 0:
        for i in range(1, num + 1):
            fact *= i
    return fact

def pois_dist(average_success, actual_success):
    prob_k_success = (average_success ** actual_success * e ** (-average_success)) / factor(actual_success)
    return prob_k_success

avgrep_a = i1[0]
avgrep_b = i1[1]

X2 = avgrep_a + avgrep_a ** 2
Y2 = avgrep_b + avgrep_b ** 2

c_a = 160 + 40 * X2
c_b = 128 + 40 * Y2

print(round(c_a, 3))
print(round(c_b, 3))
