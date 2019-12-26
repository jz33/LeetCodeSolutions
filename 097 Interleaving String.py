'''
97. Interleaving String
https://leetcode.com/problems/interleaving-string/

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
'''
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = set() # set((next index in s1, next index in s2))
        dp.add((0,0))
        for c in s3:
            dpNext = set()
            
            for i,j in dp:
                if i < len(s1) and c == s1[i]:
                    dpNext.add((i+1,j))
                if j < len(s2) and c == s2[j]:
                    dpNext.add((i,j+1))
                    
            if not dpNext:
                return False           
            dp = dpNext 
            
        return True
