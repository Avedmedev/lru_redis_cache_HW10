from functools import wraps


class LRURedisCache:
    def __init__(self, client,  capacity: int = 100):
        self.capacity = capacity
        self.client = client
        self.lru = {}
        self.tm = 0

    def __del__(self):
        pass

    def __get(self, key):
        if self.client.exists(key):
            self.lru[key] = self.tm
            self.tm += 1
            return self.client.get(key).decode()
        else:
            return -1

    def __set(self, key, value):
        if len(self.lru) >= self.capacity:
            old_key = min(self.lru.keys(), key=lambda k: self.lru[k])
            self.client.unlink(old_key)
            self.lru.pop(old_key)
            self.__set(key, value)
        else:
            self.client.set(name=key, value=value, ex=120)
            self.lru[key] = self.tm
            self.tm += 1

    def __call__(self, func=None, capacity: int = 100):

        self.capacity = capacity

        def decorator(func):

            @wraps(func)
            def wrapper(name):
                prefix = func.__name__

                data = self.__get(prefix + "_" + str(name))
                if data == -1:
                    data = func(name)
                    self.__set(prefix + "_" + str(name), data)
                return data

            return wrapper

        if callable(func):
            return decorator(func)

        return decorator


if __name__ == '__main__':
    cache = LRURedisCache(capacity=10)
