'''
411. Minimum Unique Word Abbreviation
https://leetcode.com/problems/minimum-unique-word-abbreviation/

A string such as "word" contains the following abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Given a target string and a set of strings in a dictionary,
find an abbreviation of this target string with the smallest possible length such that
it does not conflict with abbreviations of the strings in the dictionary.

Each number or letter in the abbreviation is considered length = 1. For example, the abbreviation "a32bc" has length = 4.

Note:

In the case of multiple answers as shown in the second example below, you may return any one of them.
Assume length of target string = m, and dictionary size = n. You may assume that m ≤ 21, n ≤ 1000, and log2(n) + m ≤ 20.
Examples:

"apple", ["blade"] -> "a4" (because "5" or "4e" conflicts with "blade")

"apple", ["plain", "amber", "blade"] -> "1p3" (other valid answers include "ap3", "a3e", "2p2", "3le", "3l1").
'''
class Solution:
    '''
    Combine 320. Generalized Abbreviation & 408. Valid Word Abbreviation
    '''
    def preorder(self, word, si):
        if si >= len(word):
            return
        
        for i in range(si, len(word)):
            for width in range(1, len(word)-i+1):
                cw = str(width)
                newWord = word[:i] + cw + word[i+width:]
                self.pool.append((newWord, len(word) - width + 1))
                self.preorder(newWord, i+len(cw)+1)
    
    def generateAbbreviations(self, word: str) -> List[str]:
        self.pool = [(word, len(word))] # [(abbr, length)]
        self.preorder(word, 0)

    def isValidWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0 # index of word
        num = 0
        for a in abbr:
            if a.isalpha():
                if num > 0:
                    i += num
                    num = 0
                
                if i >= len(word) or word[i] != a:
                    return False              
                i += 1
                
            else:
                num = num * 10 + int(a)
                
        if num > 0:
            i += num
        
        return i == len(word)

    def minAbbreviation(self, target: str, dictionary: List[str]) -> str:
        self.generateAbbreviations(target)
        self.pool.sort(key = lambda x : x[1])
        
        for abbr,_ in self.pool:
            for dw in dictionary:
                if self.isValidWordAbbreviation(dw, abbr):
                    break
            else:
                return abbr
        return ''
