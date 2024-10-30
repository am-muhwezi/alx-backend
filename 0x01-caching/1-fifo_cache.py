#!/usr/bin/python3
""" Basic cache"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO cache class """
    def __init__(self):
        """ Initiliaze"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        if key is not None and item is not None:
            if key not in self.cache_data:
                self.order.append(key)
            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first = list(self.cache_data.keys())[0]
                del self.cache_data[first]
                print("DISCARD:", (first))

    def get(self, key):
        return self.cache_data.get(key, None)
