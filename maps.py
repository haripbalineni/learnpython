#map(function,data)
from random import shuffle

def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return ''.join(anagram)


words = ['beetroot','carrot','tomatoes']
anagrams = []

#using for loop
for word in words:
    anagrams.append(jumble(word))
print(anagrams)

#using comprehension

print([jumble(word) for word in words])

#using map
print(list(map(jumble,words)))



