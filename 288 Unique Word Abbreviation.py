'''
288. Unique Word Abbreviation
https://leetcode.com/problems/unique-word-abbreviation/

An abbreviation of a word follows the form <first letter><number><last letter>.
Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
     ↓
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
     ↓   ↓    ↓    ↓  ↓    
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
     ↓   ↓    ↓
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary.
A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example:

Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true
'''
def getHash(word: str) -> int:
    size = len(word)
    if size == 0:
        return 0
    elif size == 1:
        return ord(word[0])
    elif size == 2:
        return ord(word[0]) * 100 + ord(word[-1])
    else:
        return size * 10000 + ord(word[0]) * 100 + ord(word[-1])
    
class ValidWordAbbr:
    def __init__(self, dictionary: List[str]):
        book = collections.defaultdict(set) # {abbreviation hash : set(words)}
        for word in dictionary:
            h = getHash(word)
            book[h].add(word)
        self.book = book

    def isUnique(self, word: str) -> bool:
        h = getHash(word)
        return h not in self.book or len(self.book[h]) == 1 and word in self.book[h]
