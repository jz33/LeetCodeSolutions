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
    def lessThan(self, a: str, b: str, book) -> bool:
        for i in range(min(len(a), len(b))):
            ca = a[i]
            cb = b[i]
            if ca != cb:
                return book[ca] < book[cb]
        return len(a) <= len(b)
                    
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        book = dict(zip(order, range(len(order)))) # {char : index}
        for i in range(len(words)-1):
            if not self.lessThan(words[i], words[i+1], book):
                return False
        return True
