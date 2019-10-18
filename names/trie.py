class Trie:
  def __init__(self, value=None, word=False):
    self.value = value
    self.children = {}
    self.word = word