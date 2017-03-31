# File name: structures.py
# Author: Nupur Garg
# Date created: 3/31/2017
# Python Version: 3.5


from src.globals import *


class Queue(object):
    """
    Represents a queue.
    """

    def __init__(self):
        self._items = []
        self._min = None

    def empty(self):
        return self._items == []

    def enqueue(self, item):
        self._items.insert(0, item)
        if not self._min:
            self._min = item
        self._min = min(item, self._min)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    # Represents minimum visited at any point.
    def min(self):
        return self._min
