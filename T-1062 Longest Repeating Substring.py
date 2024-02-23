'''
1062. Longest Repeating Substring
https://leetcode.com/problems/longest-repeating-substring/

Given a string s, return the length of the longest repeating substrings.
If no repeating substring exists, return 0.

Example 1:

Input: s = "abcd"
Output: 0
Explanation: There is no repeating substring.

Example 2:

Input: s = "abbaba"
Output: 2
Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.

Example 3:

Input: s = "aabcaabdaab"
Output: 3
Explanation: The longest repeating substring is "aab", which occurs 3 times.

Constraints:
    1 <= s.length <= 2000
    s consists of lowercase English letters.
'''
class Solution:
    '''
    Similar method to 718. Maximum Length of Repeated Subarray
    '''
    def longestRepeatingSubstring(self, s: str) -> int:
        size = len(s)
        dp = [[0] * (size + 1) for _ in range(size + 1)]
        maxSize = 0
        for i in range(size):
            for j in range(i+1, size):
                if s[i] == s[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                    maxSize = max(maxSize, dp[i+1][j+1])
        return maxSize