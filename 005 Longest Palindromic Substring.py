'''
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''
def longestPalindrome(s: str) -> str:
    '''
    A simple DP approach
    For example:
    b a b a d
    1 1 1 1 1
     0 0 0 0
      1 0 0 
       0 0
        0
    Where dp[i][j] means whether s[i:j+1] is palindromic or not
    '''
    N = len(s)
    dp = [[False] * N for i in range(N)]

    # Result
    resLeft = 0
    resRight = 0 # inclusive
    foundInThisSize = False
    
    # Initialize substring size = 1 and 2 cases
    for i in range(N):
        dp[i][i] = True
 
    for i in range(N-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            if not foundInThisSize:
                resLeft = i
                resRight = i + 1
                foundInThisSize = True
 
    for size in range(2, N): # size + 1 means substring length
        foundInThisSize = False
        for i in range(N-size):
            dp[i][i+size] = dp[i+1][i+size-1] and (s[i] == s[i+size])
            if dp[i][i+size] and not foundInThisSize:
                resLeft = i
                resRight = i + size
                foundInThisSize = True

    return s[resLeft : resRight+1]


class Solution:
    '''
    Regular O(n^2) way
    '''
    def extend(self, s: List[str], i:int, j: int):
        '''
        Get left and right index (exclusive) expaned from i, j
        '''
        while i > -1 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i+1:j]    
    
    def longestPalindrome(self, s: str) -> str:
        # Simple O(N^2) solution
        # Result, use list first
        res = []
        ls = list(s)
        for i in range(len(ls)):
            r0 = self.extend(ls,i,i)
            if len(r0) > len(res):
                res = r0
            r1 = self.extend(ls,i,i+1)
            if len(r1) > len(res):
                res = r1
        return ''.join(res)
