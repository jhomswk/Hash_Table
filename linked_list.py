
class Linked_List_Element:
    """
    Linked-List element.
    """

    def __init__(self, key, value):
        """
        Generates a linked list element with the given key
        and value.
        """
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


    def find(self, key):
        """
        Returns an element holding key in self's sub-list.
        If no such element exists, then None is returned.
        """
        target = self
        while target and target.key != key:
            target = target.next
        return target


    def insert(self, element):
        """
        Inserts element at the beginning of self's
        linked-list.
        """
        self.prev = element
        element.next = self
        return element


    def update(self, value):
        """
        Sets self's value.
        """
        self.value = value
        return self


    def delete(self):
        """
        Deletes self from the linked-list.
        """
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        return self


    def __repr__(self):
        """
        Returns the string representation of self.
        """
        return "(k: " + str(self.key) + ", v: " + str(self.value) + ")"



class Linked_List:
    """
    Linked-List data structure.
    """

    def __init__(self):
        """
        Generates an empty linked-list.
        """
        self.head = None


    def find(self, key):
        """
        Returns the element in the linked-list holding key
        if such element exists. Returns None otherwise.
        """
        return self.head and self.head.find(key)


    def insert(self, key, value):
        """
        Inserts an element holding key and value into the
        linked-list.
        """
        element = Linked_List_Element(key, value)
        if self.head:
            self.head.insert(element)
        self.head = element
        return element


    def delete(self, key):
        """
        Deletes an element holding key k form the linked list.
        """
        target = self.find(key)
        if target:
            if target is self.head:
                self.head = target.next
            target.delete()
        return target


    def update(self, key, value):
        """
        Finds an element holding key and updates its value.
        If no such element exits, then inserts a new element
        holding key and value.
        """
        target = self.find(key)
        return target.update(value) if target else self.insert(key,value)


    def __repr__(self):
        """
        Returns the string representation of a linked-list.
        """
        rep = []
        element = self.head
        while element:
            rep.append((element.key, element.value))
            element = element.next
        return str(rep)


