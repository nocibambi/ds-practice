import time

def clock(func):
    def clocked(*args): # Define the inner function `clocked` to accept any positional argument
        t0 = time.perf_counter()
        result = func(*args) # This line to work requires the `func` free variable within the closure of `clocked`
        elapsed = time.perf_counter() - t0

        name = func.__name__

        arg_str = ', '.join(repr(arg) for arg in args)
        print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))

        return result
    return clocked
