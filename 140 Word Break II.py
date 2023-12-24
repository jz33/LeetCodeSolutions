'''
40. Word Break II
https://leetcode.com/problems/word-break-ii/

Given a string s and a dictionary of strings wordDict,
add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []

Constraints:
    1 <= s.length <= 20
    1 <= wordDict.length <= 1000
    1 <= wordDict[i].length <= 10
    s and wordDict[i] consist of only lowercase English letters.
    All the strings of wordDict are unique.
    Input is generated in a way that the length of the answer doesn't exceed 105.
'''
from typing import List

class Solution:
    '''
    DFS will scope down the problem very quickly
    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not wordDict:
            return []
        
        book = set(wordDict)
        maxSize = len(max(wordDict, key = len)) # max size of the word in dict
        solutions = {} # solution cache of s[i:]
        solutions[len(s)] = ['']
        
        def dfs(i: int) -> List[str]:
            sol = []
            if i not in solutions:
                # to make sure s[i:j] in book, then j-i <= maxSize
                for j in range(i+1, min(maxSize+i+1, len(s)+1)):
                    suffix = s[i:j]
                    if suffix in book:
                        for sub in dfs(j):
                            sol.append(suffix + (sub and ' ' + sub))
                solutions[i] = sol              
            else:
                sol = solutions[i]
            return sol
        
        return dfs(0)        


'''
Based on the simplest approach of 139. Word Break
'''
class DpEntry:
    def __init__(self, end, paths=[[]]):
        self.end = end # the prefix ends in s[:end]
        self.paths = paths

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        book = set(wordDict)
        longestWordLength = len(max(wordDict, key = len))
        dp = [DpEntry(0)]
        
        for i in range(1, len(s)+1):
            newPaths = []
            for entry in reversed(dp):
                suffixSize = i - entry.end
                # Early break based on longest word
                if suffixSize > longestWordLength:
                    break
                suffix = s[entry.end : i]
                if suffix in book:
                    newPaths += [path + [suffix] for path in entry.paths]
            if newPaths:
                dp.append(DpEntry(i, newPaths))
        
        if dp[-1].end == len(s):
            return [' '.join(path) for path in dp[-1].paths]
        else:
            return []
        
sol = Solution()
s = 'catsanddog'
wordDict = ["cat","cats","and","sand","dog"]
print(sol.wordBreak(s, wordDict))