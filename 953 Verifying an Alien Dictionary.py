'''
953. Verifying an Alien Dictionary
https://leetcode.com/problems/verifying-an-alien-dictionary/

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet,
return true if and only if the given words are sorted lexicographicaly in this alien language.

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.)
According to lexicographical rules "apple" > "app", because 'l' > '∅',
where '∅' is defined as the blank character which is less than any other character (More info).
'''
class Solution:
    def charToInt(self, ch: str) -> int:
        return ord(ch) - ord('a')
    
    def lessThan(self, a: str, b: str, book: List[int]) -> bool:
        size = min(len(a), len(b))
        for i in range(size):
            ca = a[i]
            cb = b[i]
            if ca != cb:
                ia = book[self.charToInt(ca)]
                ib = book[self.charToInt(cb)]
                if ia < ib:
                    return True
                else: # ia > ib
                    return False
        
        return len(a) <= len(b)
        
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        book = [None] * 26 # char : index
        for i, ch in enumerate(order):
            book[self.charToInt(ch)] = i
        
        for i in range(1, len(words)):
            if not self.lessThan(words[i-1], words[i], book):
                return False
        
        return True
