# From https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3
def main():
    loopnum = int(input("How many times would you like to loop?\n"))
    counter = 1
    recurr(loopnum, counter)

# def recurr(loopnum, counter):
#     if loopnum > 0:
#         print("This is loop iteration", counter)
#         recurr(loopnum - 1, counter + 1)
#     else:
#         print("The loop is complete")

def recurr(loopnum, counter):
    # With numpy (almost)
    import numpy as np

    txt = (np.tile(np.array("This is loop iteration "), loopnum))
    nums = np.arange(1, loopnum + 1)

    print(np.array([txt, nums]).T)
    print("The loop is complete")

main()
