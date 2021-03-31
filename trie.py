def insert(word):
  for i in range(len(word)):
      node = root
      for letter in word:
        if letter not in node:
          node[letter] = {}
        node = node[letter]
        node[letter] = True
      word=word[1:]

def search(find):
  node = root
  for letter in find:
    if letter not in node:
      return False
    node = node[letter]
  return True

root = {}
word = "algorithmisfun"
insert(word)

find = "fun"
if search(find) == bool(True):
  print(find, "is in the Trie.")
if search(find) == bool(False):
  print(find, "is not in the Trie.")
