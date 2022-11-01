from abc import abstractmethod, ABC
from collections import OrderedDict


class Cache(ABC):
    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def put(self, key, value):
        pass


class LIFOCache(Cache):
    def __init__(self, size):
        self._data = {}
        self._size = size

    def get(self, key):
        return self._data[key]

    def put(self, key, value):
        if len(self._data) >= self._size:
            self._data.popitem()
        self._data[key] = value

    def __str__(self):
        return str(self._data)


items_to_insert = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5
}

my_cache = LIFOCache(3)
print('===========LIFO==============')
for k, v in items_to_insert.items():
    print(f'Inserting {k}')
    my_cache.put(k, v)
    print(my_cache)


class FIFOCache(Cache):
    def __init__(self, size):
        self._data = OrderedDict()
        self._size = size

    def get(self, key):
        return self._data[key]

    def put(self, key, value):
        if len(self._data) >= self._size:
            self._data.popitem(last=False)
        self._data[key] = value

    def __str__(self):
        return str(self._data)


print('===========FIFO==============')
my_cache = FIFOCache(3)
for k, v in items_to_insert.items():
    print(f'Inserting {k}')
    my_cache.put(k, v)
    print(my_cache)
