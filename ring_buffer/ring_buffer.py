from dll_queue import Queue

class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity
    self.queue = Queue()

  def append(self, item):
    self.storage[self.current] = item
    self.current += 1
    self.current = self.current % self.capacity

  def get(self):
    return self.storage