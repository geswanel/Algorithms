# list implementation
class Node:
    """Node class for list structure.

    Attributes:
        val: value stored in node
        next: link to next node
        prev: link to previous node

    Methods:

    Example:
    """
    def __init__(self, val):
        self.val = val
        self.next: Node = None
        self.prev: Node = None

class List:
    """Doubly linked list implementation.

    Attributes:
        head `Node`: first element of list.
        tail `Node`: last element of list.
    
    Methods:

    See Also:
        Node: for information about Node
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert(self, pos : int, val):
        """Insert element at position"""
        if pos > self.size or abs(pos) >= self.size:    # size - pos index
            raise IndexError("Position out of range")

        if pos == self.size:
            self.push_back(val)
        elif pos == -self.size:
            self.push_front(val)
        else:
            if pos > 0:
                
            else:
                
        


    def push_front(self, val):
        pass

    def push_back(self, val):
        pass

    def pop_back(self):
        pass

    def pop_front(self):
        pass


List