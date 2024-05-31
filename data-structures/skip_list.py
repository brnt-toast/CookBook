import random

class SkipListNode:
    def __init__(self, key, level):
        self.key = key
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self, max_level):
        self.max_level = max_level
        self.head = SkipListNode(-1, self.max_level)
        self.level = 0 # Current Level

    def random_level(self):
        level = 0
        while random.random() < 0.5 and level < self.max_level:
            level += 1
        return level

    def insert(self, key):
        update = [None] * (self.max_level +1)
        current = self.head

        
