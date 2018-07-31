# From the book 'Problem Solving with Algorithms and Data Structures' by Brad Miller, David Ranum, Release 3.0

def main():
    # print(r_list_sum([1, 3, 5, 7, 9]))
    # print(list_sum([1, 3, 5, 7, 9]))
    # print(to_str(1453, 16))
    # print(to_str2(1453, 16))
    draw_spiral(my_turtle, 100)
    my_win.exitonclick()

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.insert(0, item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items[0]

    def size(self):
        return len(self.items)



def list_sum(num_list):
    the_sum = 0

    for i in num_list:
        the_sum += i
    return the_sum

def r_list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])

def to_str(n, base):
    print("base:{}".format(base))
    print("n:{}".format(n))

    convert_string = "0123456789ABCDEF"

    if n < base:
        return convert_string[int(n)]
    else:
        return to_str(n / base, base) + convert_string[int(n % base)]


def check_pal(phrase):
    """
    Checks whether a phrase is a palindrome or not.

    >>> check_pal('Reviled did I live, said I, as evil I did deliver')
    True
    """
    import re
    p = re.compile('\W')
    phrase = p.sub('', phrase).lower()

    # With list
    # rev = list(phrase)
    # rev.reverse()
    #
    # return list(phrase) == rev

    # With iterator
    # rev = ""
    # for i in reversed(phrase):
    #     rev += i

    # With recursion
    def srev(string):
        if len(string) == 1:
            return string[0]

        else:
            return srev(string[1:]) + string[0]

    return phrase == srev(phrase)


#import Stack
r_stack = Stack()

def to_str2(n, base):
    """Using stack"""
    print("base:{}".format(base))
    print("n:{}".format(n))

    convert_string = "0123456789ABCDEF"

    while n > 0:
        if n < base:
            r_stack.push(convert_string[int(n)])
        else:
            r_stack.push(convert_string[int(n % base)])

        n = n // base # what does this line do?

    res = ""
    while not r_stack.is_empty():
        res = res + str(r_stack.pop())

    return res

import turtle

my_turtle = turtle.Turtle()
my_win = turtle.Screen()

def draw_spiral(my_turtle, line_len):
    if line_len > 0:
        my_turtle.forward(line_len)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_len - 5)

main()
