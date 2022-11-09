
import sys
from timeit import timeit

version =  f'{sys.version_info.major}.{sys.version_info.minor}' 
print(f'{version:_^31}')
print("User Current Version:-", sys.version_info.major  )




def loops():
    "-".join(str(n) for n in range(100))
    [x+x for x in range(100)]
    [x^x for x in range(100)]
    


out = timeit(lambda: loops(), number=10000)
print(f'{"loops":.<15}{out:.>15.4f}s')



