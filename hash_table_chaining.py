from linked_list import Linked_List
from sys import maxsize as max_int
from random import randrange
from math import log

class Hash_Table:
    """
    Hash-Table.
    Collision resolution: chaining.
    Load factor: [0.25, 1]
    """

    def __init__(self):
        """
        Generates an empty hash-table.
        """
        self.table = [Linked_List() for _ in range(4)]
        self.hash_size = 2
        self.min_size = 1
        self.max_size = 4
        self.num_keys = 0
        self.rand = randrange(1, max_int)
        self.word_size = int(log(max_int,2))
        self.h = lambda key: (self.rand*key % max_int) >> (self.word_size - self.hash_size)


    def find(self, key):
        """
        Returns the pair (key, value) if key is present in
        the hash-table, and None otherwise.
        """
        return self.table[self.h(key)].find(key)


    def insert(self, key, value):
        """
        Inserts the pair (key, value) in the hash-table. 
        """
        if self.find(key):
            return None

        if self.num_keys == self.max_size:
            self.expand()

        self.num_keys += 1

        return self.table[self.h(key)].insert(key, value)


    def delete(self, key):
        """
        Deletes the pair (key, value) from the hash-table.
        """
        target = self.table[self.h(key)].delete(key)

        if target:
            self.num_keys -= 1

            if self.num_keys == self.min_size and self.hash_size > 2:
                self.contract()

        return target


    def update(self, key, value):
        """
        Finds the pair holding key in the hash-table and updates
        its value. If no such element exits, then inserts the 
        given pair.
        """
        target = self.find(key)

        if target:
            target.update(key)

        else:
            target = self.insert(key, value)

        return target


    def expand(self):
        """
        Expands the hash-table doubling its size.
        """
        self.hash_size += 1
        self.min_size *= 2
        self.max_size *= 2
        self.rehash()


    def contract(self):
        """
        Contracts the hash-table halving its size
        """
        self.hash_size -= 1
        self.min_size //= 2
        self.max_size //= 2
        self.rehash()


    def rehash(self):
        """
        Rehashes all keys in the hash-table.
        """
        self.num_keys = 0
        table = self.table
        self.table = [Linked_List() for slot in range(self.max_size)]

        for slot in table:
            element = slot.head
            while element:
                self.insert(element.key, element.value)
                element = element.next


    def __repr__(self):
        """
        Represents a hash-table.
        """
        return "\n".join("  {}: {}".format(key, chain) for (key, chain) in enumerate(self.table))

