
class Hash_Table:
    """
    Hash-Table.
    Collision resolution: open addressing.
    Load factor: [0.25, 0.5]
    """

    def __init__(self):
        """
        Generates an empty hash-table.
        """
        self.num = 0
        self.size = 8
        self.marked = 0
        self.num_min = 1
        self.size_min = 8
        self.marked_max = 4
        self.h1 = lambda k: k % self.size
        self.h2 = lambda k: 1 + 2*(k % self.marked_max)
        self.table = [None for _ in range(self.size)]


    def probing_sequence(self, key):
        """
        Generates a sequence of pairs (slot, element) according
        to the probing sequence of key.
        """
        slot = self.h1(key)
        step = self.h2(key)
        for access in range(self.size):
            yield (slot, self.table[slot])
            slot = self.h1(slot + step)


    def find(self, key):
        """
        Returns the pair (key, value), if key is present in
        the hash-table, and None otherwise.
        """
        for (slot, element) in self.probing_sequence(key):
            if element == None or element[0] == key:
                return element

        return None


    def insert(self, key, value):
        """
        Inserts the pair (key, value), if key is not present
        in the hash-table. Otherwise, updates the value of
        the pair holding key.
        """
        probing_sequence = self.probing_sequence(key)
        for (slot, element) in probing_sequence:

            if element == None:

                if element == None:
                    self.num += 1
                    self.marked += 1
                    self.table[slot] = (key, value)

                    if self.marked > self.marked_max:
                        self.expand()
                return

            elif element == "D":
                self.table[slot] = (key, value)

                for (slot, element) in probing_sequence:

                    if element == None:
                        self.num += 1
                        return

                    elif element[0] == key:
                        self.table[slot] = "D"
                        return
                return

            elif element[0] == key:
                self.table[slot][1] = value
                return


    def delete(self, key):
        """
        Deletes the pair (key, value) from the hash-table.
        """
        for (slot, element) in self.probing_sequence(key):

            if element == None:
                return

            elif element[0] == key:
                self.num -= 1
                self.table[slot] = "D"

                if self.num <= self.num_min and self.size > self.size_min:
                    self.contract()
                return


    def rehash(self):
        """
        Rehashes all the elements in the hash-table.
        """
        self.num = 0
        self.marked = 0

        table = self.table
        self.table = [None for slot in range(self.size)]

        for element in table:
            if element and element != "D":
                self.insert(*element)


    def expand(self):
        """
        Expands the hash-table doubling its size.
        """
        self.size *= 2
        self.num_min *= 2
        self.marked_max *= 2
        self.rehash()


    def contract(self):
        """
        Contracts the hash-table halving its size.
        """
        self.size //= 2
        self.num_min //= 2
        self.marked_max //= 2
        self.rehash()


    def __repr__(self):
        """
        Represents the hash-table.
        """
        def showItem(item):
            """
            Returns a string representing item.
            """
            return "" if item == None else "DELETED" if item == "D" else item

        return "\n".join("  {}: [{}]".format(key, showItem(item)) for (key, item) in enumerate(self.table))

