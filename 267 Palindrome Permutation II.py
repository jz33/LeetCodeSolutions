'''
267. Palindrome Permutation II
https://leetcode.com/problems/palindrome-permutation-ii/

Given a string s, return all the palindromic permutations (without duplicates) of it.
Return an empty list if no palindromic permutation could be form.

Example 1:

Input: "aabb"
Output: ["abba", "baab"]
Example 2:

Input: "abc"
Output: []
'''
from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[str]) -> List[List[str]]:
        '''
        This is from 47. Permutations II
        '''
        perms, newPerms = [[]], []      
        for e in nums:
            for row in perms:
                
                # This basic idea is to insert e onto all positions
                # of previous permutation
                for i in range(len(row) + 1):
                    newPerms.append(row[:i] + [e] + row[i:])
                    
                    # This is the only added line to handle duplicates
                    if i < len(row) and row[i] == e: break 
                    
            perms, newPerms = newPerms, []
        return perms
    
    def generatePalindromes(self, s: str) -> List[str]:
        histo = Counter(s)
        half = []
        oddy = None
        for k,v in histo.items():
            if v % 2 == 1:
                if oddy is not None:
                    return []
                oddy = k
            half += [k] * (v // 2)
        
        res = []
        for left in self.permuteUnique(half):
            if not oddy:
                res.append(''.join(left) + ''.join(left[::-1]))
            else:
                res.append(''.join(left) + oddy + ''.join(left[::-1]))
        return res
