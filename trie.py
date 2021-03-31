def insert(word):
  for i in range(len(word)):      #loop for the step again after slice
      node = root
      for letter in word:         #loop for every letter
        if letter not in node:
          node[letter] = {}       #create new node
        node = node[letter]
        node[letter] = True       #set the node for every letter to true
      word=word[1:]               #slice the front letter by 1

def search(find):
  node = root 
  for letter in find:             #loop for every letter
    if letter not in node:
      return False                #check if the letter is not in trie
    node = node[letter]
  return True                     #the word is in trie

root = {}
word = "algorithmisfun"
insert(word)

find = "fun"
if search(find) == bool(True):
  print(find, "is in the Trie.")
if search(find) == bool(False):
  print(find, "is not in the Trie.")
