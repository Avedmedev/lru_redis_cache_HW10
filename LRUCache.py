

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.lru = {}
        self.tm = 0

    def get(self, key):
        if key in self.cache:
            self.lru[key] = self.tm
            self.tm += 1
            return self.cache[key]
        else:
            return -1

    def set(self,  key, value):
        if len(self.cache) > self.capacity:
            old_key = min(self.lru.keys(), key=lambda k: self.lru[k])
            self.cache.pop(old_key)
            self.lru.pop(old_key)
        else:
            self.cache[key] = value
            self.lru[key] = self.tm
            self.tm += 1

        print(f"LRU: {self.lru}")
        print(f"CACHE: {self.cache}")
