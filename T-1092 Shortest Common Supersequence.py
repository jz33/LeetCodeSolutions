'''
1092. Shortest Common Supersequence 
https://leetcode.com/problems/shortest-common-supersequence/

Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.
If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0)
results in the string s.

Example 1:

Input: str1 = "abac", str2 = "cab"
Output: "cabac"
Explanation: 
str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
The answer provided is the shortest such string that satisfies these properties.

Example 2:

Input: str1 = "aaaaaaaa", str2 = "aaaaaaaa"
Output: "aaaaaaaa"

Constraints:
    1 <= str1.length, str2.length <= 1000
    str1 and str2 consist of lowercase English letters.
'''
class Solution:
    '''
    Based on 1143. Longest Common Subsequence
    '''
    def longestCommonSubsequence(self, x: str, y: str) -> int:
        dp = [[''] * (len(y)+1) for _ in range(len(x)+1)]
        for i in range(len(x)):
            for j in range(len(y)):
                if x[i] == y[j]:
                    dp[i+1][j+1] = dp[i][j] + x[i]
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j], key=len)
        return dp[-1][-1]

    def shortestCommonSupersequence(self, x: str, y: str) -> str:
        result = []
        lcs = self.longestCommonSubsequence(x, y)
        xi, yi = 0, 0
        for c in lcs:
            # No need to check boundary of xi, yi, as lcs must be their subsequence
            while c != x[xi]:
                result.append(x[xi])
                xi += 1
            while c != y[yi]:
                result.append(y[yi])
                yi += 1
            result.append(c)
            xi, yi = xi + 1, yi + 1
        return ''.join(result) + x[xi:] + y[yi:]