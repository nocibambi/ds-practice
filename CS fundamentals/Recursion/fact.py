# From https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3


def main():
    num = int(input("Please enter a non-negative integer.\n"))
    # num  = np.arange(10)
    fact = factorial(num)
    print("The factorial of", num,  "is", fact)

# def factorial(num):
#     if num == 0:
#         return 1
#     else:
#         return num * factorial(num - 1)

import numpy as np

def factorial(num):
    num = np.where(num == 0, 1, np.prod(np.arange(1, num + 1)))
    return num

main()
