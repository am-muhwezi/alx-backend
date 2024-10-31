#!/usr/bin/python3
""" Basic cache"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO cache class """
    def __init__(self):
        """ Initiliaze"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first, _ = self.cache_data.popitem(False)
            print("DISCARD:", (first))

    def get(self, key):
        return self.cache_data.get(key, None)
