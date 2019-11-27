'''
1216. Valid Palindrome III
https://leetcode.com/problems/valid-palindrome-iii/

Given a string s and an integer k, find out if the given string is a K-Palindrome or not.

A string is K-Palindrome if it can be transformed into a palindrome by removing at most k characters from it.

Example 1:

Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.
'''
class Solution:
    def longestCommonSubsequence(self, a: str, b: str) -> int:
        if len(a) < len(b):
            a, b = b, a
        
        dp = [0] * len(b) # Use shorter buffer
        for i in range(len(a)):
            left = 0
            topLeft = 0
            for j in range(len(b)):
                top = dp[j]
                if a[i] == b[j]:
                    dp[j] = topLeft + 1
                else:
                    dp[j] = max(top, left)
                left = dp[j]
                topLeft = top
        return dp[-1]
    
    def longestPalindromicSubsequence(self, a: str) -> int:
        return self.longestCommonSubsequence(a, a[::-1])
        
    def isValidPalindrome(self, s: str, k: int) -> bool:
        return self.longestPalindromicSubsequence(s) + k >= len(s)
