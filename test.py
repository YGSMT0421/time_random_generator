from time import perf_counter
from random import Random

from time_random import TimeRandom, TimeRandomOrigin

def test(cls, description = None):
    inst = cls()
    if description is None:
        description = cls.__name__
    t0 = perf_counter()
    result = [inst.random() for _ in range(100_0000)]
    time = perf_counter() - t0
    print(f'''----- {description} -----
    average: {sum(result) / len(result)}
    result length: {len(result)}
    spent time: {time}s''')

if __name__ == '__main__':
    print('Test start.\n')
    test(Random)
    test(TimeRandomOrigin)
    test(TimeRandom)
    print('\nTest end.')