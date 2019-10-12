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
# Regular dp approach
class Solution:
    def numDecodings(self, src: str) -> int:
        if len(src) == 0:
            return 0
        if src[0] == '0':
            return 0
        
        if len(src) == 1:
            return 0 if src[0] == '0' else 1
        
        # Discuss the first 2 chars
        dp = [0] * len(src)
        dp[0] = 1
        
        first2 = int(src[:2])
        if first2 <= 26:
            dp[1] += 1
        if src[1] != '0':
            dp[1] += 1
        
        # Discuss src[2:]
        for i in range(2, len(src)):
            first2 = int(src[i-1:i+1])
            if src[i] == '0':
                if src[i-1] == '0' or first2 > 26:
                    return 0
                else:
                    dp[i] = dp[i-2]             
            else:
                if src[i-1] == '0' or first2 > 26:
                    dp[i] = dp[i-1]
                else:
                    dp[i] = dp[i-1] + dp[i-2]
                    
        return dp[-1]
       
# A tricky DP approach, use only constant memory
def dp(src):
    if len(src) < 1: return 0
    if len(src) == 1: return 0 if src[0] == '0' else 1
    if src[0] == '0': return 0
     
    # the buffer is of size 3
    buf = [1,0,1]
    j = 0
    for i in xrange(1,len(src)):
        j = (j+1) % 3
        n1 = (int(src[i-1]) - int('0'))*10 + int(src[i]) - int('0')
        if src[i] == '0':
            if src[i-1] == '0': return 0
            elif n1 > 26: return 0
            else: buf[j] = buf[j-2]
        else:
            if src[i-1] == '0': buf[j] = buf[j-1]
            elif n1 > 26: buf[j] = buf[j-1]
            else : buf[j] = buf[j-1] + buf[j-2]
    return buf[j]
