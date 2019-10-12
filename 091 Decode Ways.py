'''
91. Decode Ways
https://leetcode.com/problems/decode-ways/

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''
class Solution:
    def numDecodings(self, src: str) -> int:
        if len(src) == 0:
            return 0
        if src[0] == '0':
            return 0      
        if len(src) == 1:
            return 1
        
        # Use only 3 slots array, because we only care about i, i-1, i-2
        dp = [1, 0, 1]
        j = 0
        for i in range(1, len(src)):
            j = (j + 1) % 3
            first2 = int(src[i-1:i+1])
            
            if src[i] == '0':
                if src[i-1] == '0' or first2 > 26:
                    return 0
                else:
                    dp[j] = dp[j-2]             
            else:
                if src[i-1] == '0' or first2 > 26:
                    dp[j] = dp[j-1]
                else:
                    dp[j] = dp[j-1] + dp[j-2]
        
        return dp[j]     
