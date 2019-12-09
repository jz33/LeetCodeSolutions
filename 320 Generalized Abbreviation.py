'''
320. Generalized Abbreviation
https://leetcode.com/problems/generalized-abbreviation/

Write a function to generate the generalized abbreviations of a word. 

Note: The order of the output does not matter.

Example:

Input: "word"
Output:
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
'''
class Solution:
    def backtrack(self, word, si):
        if si >= len(word):
            return
        
        # Be careful of the indexes!
        for i in range(si, len(word)):
            for c in range(1, len(word)-i+1):
                cs = str(c)
                newWord = word[:i] + cs + word[i+c:]
                self.pool.append(newWord)
                self.backtrack(newWord, i+len(cs)+1)
    
    def generateAbbreviations(self, word: str) -> List[str]:
        self.pool = [word]
        self.backtrack(word, 0)
        return self.pool
