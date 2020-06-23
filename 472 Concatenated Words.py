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
    def wordBreak(self, word: str, book: 'set[str]') -> bool:
        if not book:
            return False
        
        size = len(word)
        dp = [True] + [False] * size

        for i in range(1, size + 1):
            dp[i] = any(dp[j] and word[j:i] in book for j in range(i))
  
        return dp[-1]
    
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        # The trick of performance gain is to sort words by length, and so
        # shorter words come to front. And for finding word part (word break),
        # only use visited words as book
        words.sort(key = lambda x : len(x))
        book = set()
        res = []
        for word in words:
            if self.wordBreak(word, book):
                res.append(word)
            book.add(word)
        return res
