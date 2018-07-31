# From https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3
num = 0

def main():
    counter(num)

def counter(num):
    print(num)
    num += 1
    counter(num)

main()
