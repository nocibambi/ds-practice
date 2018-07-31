# From https://en.wikibooks.org/wiki/Non-Programmer%27s_Tutorial_for_Python_3

def main():
    # i = int(input("Please enter a non-negative integer.\n"))
    i = crazy(1)
    print(next(i))

def crazy(min_):
    yield min_
    g = crazy(min_+1)

    while True:
        yield next(g)
        yield min_

main()
