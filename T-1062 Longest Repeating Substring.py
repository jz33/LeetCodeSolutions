'''
1062. Longest Repeating Substring
https://leetcode.com/problems/longest-repeating-substring/

Given a string S, find out the length of the longest repeating substring(s).
Return 0 if no repeating substring exists.

Example 1:

Input: "abcd"
Output: 0
Explanation: There is no repeating substring.

Example 2:

Input: "abbaba"
Output: 2
Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.

Example 3:

Input: "aabcaabdaab"
Output: 3
Explanation: The longest repeating substring is "aab", which occurs 3 times.

Example 4:

Input: "aaaaa"
Output: 4
Explanation: The longest repeating substring is "aaaa", which occurs twice.

Note:

The string S consists of only lowercase English letters from 'a' - 'z'.
1 <= S.length <= 1500
'''
class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        if len(S) < 2:
            return 0
        
        size = len(S)
        
        # dp[i][j] does NOT record the longest substring in S[i : j] range,
        # but rather the repeated substring S[...i] == S[...j], i.e., the
        # longest reapting substring ends in i (and thus j)
        dp = [[0] * (size + 1) for _ in range(size + 1)]

        for i in range(size):
            for j in range(i + 1, size):
                if S[i] == S[j]:
                    # If S[i] == S[j] and S[i-1] == S[j-1],
                    # then S[i-1...i] == S[j-1....j] is repeating string,
                    # thus the count can increase
                    dp[i + 1][j + 1] = dp[i][j] + 1;

        return max(dp[i][j] for i in range(size + 1) for j in range(size + 1))
