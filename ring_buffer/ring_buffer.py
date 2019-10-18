import sys
sys.path.append('../reverse')
from reverse import LinkedList

class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity
    self.list = LinkedList()

  def append(self, item):
    self.storage[self.current] = item
    self.current += 1
    self.current = self.current % self.capacity

  def get(self):
    return self.storage