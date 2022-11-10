import sys
from timeit import timeit
from functools import cache

version =  f'{sys.version_info.major}.{sys.version_info.minor}' 
print(f'{version:_^31}')


def loops():
    "-".join(str(n) for n in range(100))
    [x+x for x in range(100)]
    [x^x for x in range(100)]

out = timeit(lambda: loops(), number=10000)
print(f'{"loops":.<15}{out:.>15.4f}s')


def maps():
    {y:x for x in range(100) for y in range(100)}
    


out = timeit(lambda: maps(), number=10000)
print(f'{"maps":.<15}{out:.>15.4f}s')

@cache
def fib(x):
    if x < 1:
        return x
    return fib(x-1) + fib(x-2)


out = timeit(lambda: fib(10), number=10000)
print(f'{"fib":.<15}{out:.>15.4f}s')