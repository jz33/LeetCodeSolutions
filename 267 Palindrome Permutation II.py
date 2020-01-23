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
    def backtrack(self, histo: 'Counter', sofar: List[str]):
        if len(sofar) == self.size:
            self.pool.append(''.join(sofar))
        else:
            newHisto = copy.deepcopy(histo)
            for k,v in histo.items():
                # To avoid duplicate, select only 1 char from a pair
                sofar.append(k)
                newHisto[k] -= 1
                if newHisto[k] == 0:
                    del newHisto[k]

                self.backtrack(newHisto, sofar)

                sofar.pop()
                newHisto[k] += 1
            
    def permutations(self, s: List[str]) -> List[str]:
        '''
        Similar to Combination Sum II
        '''
        histo = Counter(s)
        self.size = len(s)
        self.pool = []
        self.backtrack(histo, [])
        return self.pool
    
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
        for left in self.permutations(half):
            if not oddy:
                res.append(left + left[::-1])
            else:
                res.append(left + oddy + left[::-1])
        return res
