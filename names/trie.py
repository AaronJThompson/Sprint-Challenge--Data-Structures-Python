class Trie:
  def __init__(self, value=None, word=False):
    self.value = value
    self.children = {}
    self.word = word

  def insert_string(self, string, idx=0):
    if not idx < len(string):
      return
    char = string[idx]
    if char in self.children:
      child = self.children[char]
      if len(string) == idx + 1:
        child.word = True
      else:
        child.insert_string(string, idx + 1)
    else:
      trie = Trie(char)
      self.children[char] = trie
      if len(string) == idx + 1:
        trie.word = True
      else:
        trie.insert_string(string, idx + 1)
      
  def __search_string__(self, string, idx):
    if not idx < len(string):
      return False
    elif len(string) == idx + 1:
      if string[idx] == self.value and self.word:
        return True
      else:
        return False
    else:
      char = string[idx + 1]
      if char in self.children:
        return self.children[char].__search_string__(string, idx + 1)
    return False