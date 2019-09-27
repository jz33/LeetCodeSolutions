'''
1143. Longest Common Subsequence
Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted
without changing the relative order of the remaining characters.
(eg, "ace" is a subsequence of "abcde" while "aec" is not).
A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:

Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.
'''
class Solution:
    def longestCommonSubsequence(self, x: str, y: str) -> int:
        # dp[i][j] means the longest common subsequence of x[:i+1], y[j+1]
        dp = [[0] * (len(y)+1) for _ in range(len(x)+1)]
        
        for i in range(len(x)):
            for j in range(len(y)):
                if x[i] == y[j]:
                    dp[i+1][j+1] = 1 + dp[i][j]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        
        return dp[len(x)][len(y)]
