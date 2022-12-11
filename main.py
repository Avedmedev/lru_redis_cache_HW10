import time
from LRURedisCache import LRURedisCache

from connection import client


cache = LRURedisCache(client)


@cache
def func_(num):
    result = num ** 2
    print('Computing ...')
    time.sleep(3)
    return result


@cache(capacity=10)
def func_3(num):
    result = num ** 3
    print('Computing ...')
    time.sleep(3)
    return result


@cache(capacity=2)
def func_4(num):
    result = num ** 4
    print('Computing ...')
    time.sleep(3)
    return result


if __name__ == '__main__':
    print(func_(11))
    print(func_(11))
    print(func_3(11))
    print(func_4(11))
    print(func_4(12))
    print(func_4(11))
    print(func_4(12))
