import sys
sys.path.append('../reverse')
from reverse import Node

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0
    
    def __len__(self):
        return self.length

    def add_to_head(self, value):
        node = Node(value)
        node.set_next(self.head)
        if self.tail is None:
            self.tail = node
        self.length += 1
