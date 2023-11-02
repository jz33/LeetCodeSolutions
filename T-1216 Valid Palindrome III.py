'''
1216. Valid Palindrome III
https://leetcode.com/problems/valid-palindrome-iii/

Given a string s and an integer k, return true if s is a k-palindrome.

A string is k-palindrome if it can be transformed into a palindrome by removing at most k characters from it.

Example 1:

Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.

Example 2:

Input: s = "abbababa", k = 1
Output: true

Constraints:
    1 <= s.length <= 1000
    s consists of only lowercase English letters.
    1 <= k <= s.length
'''
def longestCommonSubsequence(x: str, y: str) -> int:
    # Same idea as 1143. Longest Common Subsequence,
    # dp[i][j] means the longest common subsequence of x[:i+1], y[j+1]
    dp = [[0] * (len(y)+1) for _ in range(len(x)+1)]
    
    for i in range(len(x)):
        for j in range(len(y)):
            if x[i] == y[j]:
                dp[i+1][j+1] = 1 + dp[i][j]
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    
    return dp[len(x)][len(y)]

class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        return longestCommonSubsequence(s, s[::-1]) + k >= len(s)
