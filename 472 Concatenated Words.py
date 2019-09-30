'''
472. Concatenated Words
https://leetcode.com/problems/concatenated-words/

Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.
A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

Example:

Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

Explanation:

"catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
 "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
"ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".

'''
class Solution:
    def find(self, word: str, book: 'set[str]') -> bool:
        if len(book) == 0:
            return False
        
        size = len(word)
        
        # dp[i] means if word[:i] is in Concatenated word
        dp = [False] * (size + 1)
        dp[0] = True
        
        # Iterate all substrings
        # Same method like Word Break
        for i in range(1, size+1):
            for j in range(size):
                dp[i] = dp[j] and word[j:i] in book
                if dp[i]:
                    break
        
        return dp[-1]
    
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # Only need to refer the words that are already processed
        # As shorter word is sorted to front
        dones = set()
        words.sort(key = lambda x : len(x))
        
        res = []
        for word in words:
            if self.find(word, dones):
                res.append(word)
            dones.add(word)
        return res
