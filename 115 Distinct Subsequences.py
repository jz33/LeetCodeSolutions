'''
115. Distinct Subsequences
https://leetcode.com/problems/distinct-subsequences/

Given two strings s and t, return the number of distinct subsequences of s which equals t.
The test cases are generated so that the answer fits on a 32-bit signed integer.

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from s.
rabbbit
rabbbit
rabbbit

Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from s.
babgbag
babgbag
babgbag
babgbag
babgbag

Constraints:
    1 <= s.length, t.length <= 1000
    s and t consist of English letters.
'''
class Solution:
    def numDistinct(self, source: str, target: str) -> int:
        # dp[s][t] is the distinct count of src[:s] to tag[:t]
        dp = [[0] * (len(target)+1) for _ in range(len(source)+1)]
 
        # If target is empty, there is always 1 distinct subsequence.
        # This includes any source[:] and empty target case.
        for s in range(len(source)+1):
            dp[s][0] = 1

        for s in range(len(source)):
            for t in range(len(target)):
                if source[s] == target[t]:
                    dp[s+1][t+1] = dp[s][t+1] + dp[s][t]
                else:
                    dp[s+1][t+1] = dp[s][t+1]
                    
        return dp[-1][-1]
