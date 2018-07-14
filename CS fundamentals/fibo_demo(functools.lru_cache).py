import functools
from clockdeco import clock

@functools.lru_cache() # This line alone does the memoization
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)

if __name__ == '__main__':
    print(fibonacci(6))
