'''
131. Palindrome Partitioning
https://leetcode.com/problems/palindrome-partitioning/

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''
from functools import lru_cache

class Solution:
    @lru_cache(None)
    def isPalindromic(self, s: str) -> bool:
        return s == s[::-1]
    
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 1:
            return [[s]]
        
        result = []
        if self.isPalindromic(s):
            result.append([s])
            
        for i in range(1, len(s)):
            if self.isPalindromic(s[:i]):
                for child in self.partition(s[i:]):
                    result.append([s[:i]] + child)  
 
        return result
