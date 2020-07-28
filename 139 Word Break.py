'''
139. Word Break
https://leetcode.com/problems/word-break/

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
             
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''
class Solution:
    '''
    A dfs solution
    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict:
            return False
        
        book = set(wordDict)
        maxSize = len(max(wordDict, key = len)) # max size of the word in dict
        solutions = {} # solution cache of s[i:]
        solutions[len(s)] = True
        
        def dfs(i: int) -> bool:
            if i not in solutions:
                # to make sure s[i:j] in book, then j-i <= maxSize
                solutions[i] = any(s[i:j] in book and dfs(j) for j in range(i+1, min(maxSize+i+1, len(s)+1)))              
            return solutions[i]
        
        return dfs(0)


class Solution:
    '''
    An iterative solution with max length early break
    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not wordDict:
            return False
        
        book = set(wordDict)
        maxSize = len(max(wordDict, key = len)) # max size of the word in dict
        
        # dp[i] means whether s[:i] is composable
        dp = [True] + [False] * len(s)
        for i in range(1, len(s)+1):
            dp[i] = any(dp[j] and s[j:i] in book for j in range(max(0, i-maxSize), i))
            
        return dp[-1]

     
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        Simplest iterative solution
        '''
        if not wordDict:
            return False
        
        book = set(wordDict)
        
        # dp[i] means word[:i] is composable or not
        dp = [True] + [False] * len(s)
        for i in range(1, len(s)+1):
            dp[i] = any(dp[j] and s[j:i] in book for j in range(i))
        return dp[-1]
      
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        '''
        Simplest iterative solution, faster than above
        '''
        if not wordDict:
            return False
        
        book = set(wordDict)
        
        # If i in dp, it means word[:i] is composable
        dp = [0]
        for i in range(1, len(s)+1):
            if any(s[j:i] in book for j in dp):
                dp.append(i)

        return dp[-1] == len(s)
