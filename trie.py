def insert(word):
  for i in range(len(word)):
      node = root
      for letter in word:
        if letter not in node:
          node[letter] = {}
        node = node[letter]
        node[letter] = True

      word=word[1:]

def search(word):
  node = root
  for letter in word:
    if letter not in node:
      return False
    node = node[letter]
  return True

root = {}
words = []
n = int(input("Enter number of words : "))
print("Enter the words : ")
for i in range(0, n):
    name1 = input()
    words.append(name1)
for word in words:
  insert(word)

print("What you want to search?")
cari=input()
print(search(cari))

if search(cari) == bool(True):
  print(cari, "is in the Trie.")
if search(cari) == bool(False):
  print(cari, "is not in the Trie.")