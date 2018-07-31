# A tail-recursive function returns a call only to itself. For tail-recursive languages the computer, in such a case, does not need to track the previous results.
# Most recursive functions can be transformed into a tail-call form

def factorial(n):
    if n == 0: return 1
    else: return factorial(n - 1) * n # Almost a trail-call but the multiplication is outside of the function

def trail_factorial(n, accumulator=1):
    if n == 0: return 1
    else: return trail_factorial(n-1, accumulator * n) #

# But python does not support tail-call optimization, mostly because it is built around iteration. Python does not support it by default.

# We can use a decorator.
@ tail recursive
def trail__dec_fact(n, accumulator=1):
    if n == 0:
        return accumulator
    recurse(n-1, accumulator=accumulator * n)


class Recurse(Exception):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

def recurse(*args, **kwargs):
    raise Recurse(*args, **kwargs)

def tail_recursive(f):
    def decorated(*args, **kwargs):
        while True:
            try:
                return f(*args, **kwargs)
            except Recurse as r:
                args = r.args
                kwargs = r.kwargs
                continue
return decorated
