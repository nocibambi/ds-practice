import turtle
import numpy as np


def main():
    t = turtle.Turtle()
    myWin = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(100)
    t.down()
    t.color("green")
    tree(75,t)
    myWin.exitonclick()


def tree(branchLen,t):
    if branchLen < 20:
        t.color("red")
    else:
        t.color("green")

    if branchLen > 5:
        t.forward(branchLen)
        t.right(np.random.randint(19, 21))

        tree(branchLen-np.random.randint(10, 20),t)
        if branchLen < 20:
            t.color("red")
        else:
            t.color("green")

        t.left(np.random.randint(19, 21) * 2)

        tree(branchLen-np.random.randint(10, 20),t)
        if branchLen < 20:
            t.color("red")
        else:
            t.color("green")

        t.right(np.random.randint(19, 21))
        t.backward(branchLen)




main()
