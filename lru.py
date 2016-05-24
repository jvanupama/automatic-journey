from datetime import *
from time import sleep


class LRUCacheSample(object):
    """Sample data structure of items in cache"""
    def __init__(self, key, item):
        self.key = key
        self.item = item
        self.timestamp = datetime.now()


class LRUCache(object):
    """A sample class that implements LRU caching algorithm"""

    def __init__(self, length, delta=None):
        self.length = length
        self.delta = delta # delta value is for measuring the difference in time
        self.hash = {}
        self.item_list = []

    def insertItem(self, item):
        """Insert new items to cache"""

        if item.key in self.hash:
            # Move the existing item to the front of
            # item_list.
            for i, it in enumerate(self.item_list):
                if it == item:
                    self.item_list.insert(0, item)
                    self.item_list[i + 1:] = self.item_list[i + 2:]
                    break
        else:
            # Check if the length of cache exceeds the
            # upper bound which is the current length of the cache (4 in this example).
            if len(self.item_list) > self.length:
                self.removeItem(self.item_list[-1])

            # If new item, append it to
            # the front.
            self.hash[item.key] = item
            self.item_list.insert(0, item)

    def removeItem(self, item):
        """Remove  invalid items"""

        del self.hash[item.key]
        del self.item_list[self.item_list.index(item)]

    def validateItem(self):
        """Check if the items are still valid."""

        

        now = datetime.now()
        remove_list = []
        for it in self.item_list:
            time_delta = now - it.timestamp
            if time_delta.seconds > self.delta:
                remove_list.append(it)
        map(lambda x: self.removeItem(x), remove_list)

# Testing the Cache with 4 sample items
# Can test for inserting an item and validating the items after sometime based on LRU 
def print_cache(cache):
    for i, item in enumerate(cache.item_list):
        print ("index: {0} "
                "key: {1} "
                "item: {2} "
                "timestamp: {3}".format(i,
                                       item.key,
                                       item.item,
                                       item.timestamp))

one = LRUCacheSample(1, 'one')
two = LRUCacheSample(2, 'two')
three = LRUCacheSample(3, 'three')
four = LRUCacheSample(4, 'four')

print ("Initial cache items ")
cache = LRUCache(length=4, delta=5)
cache.insertItem(one)
cache.insertItem(two)
cache.insertItem(three)
cache.insertItem(four)
print_cache(cache)
print ("-" * 20)

print ("Insert a existing item: {0}.".format(one.key))
cache.insertItem(one)
print_cache(cache)
print ("-" * 20)

print ("Insert another existing item: {0}.".format(two.key))
cache.insertItem(two)
print_cache(cache)
print ("-" * 20)

print ("Insert another existing item: {0}.".format(two.key))
cache.insertItem(two)
print_cache(cache)
print ("-" * 20)

print ("Validate items after a period of time")
sleep(6) # waits for 6 seconds
cache.validateItem()
print_cache(cache)
print ("#" * 20)
        

        
