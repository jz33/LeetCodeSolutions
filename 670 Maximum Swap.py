'''
670. Maximum Swap
https://leetcode.com/problems/maximum-swap/

Given a non-negative integer, you could swap two digits at most once to get the maximum valued number.
Return the maximum valued number you could get.

Example 1:

Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:

Input: 9973
Output: 9973
Explanation: No swap.
Note:

The given number is in the range [0, 108]
'''
class Solution:
    def maximumSwap(self, num: int) -> int:
        '''
        At a position i, you need the max digit from i till right.
        If there are multiple, need the right most max.
        '''
        s = str(num)
        ms = [None] * len(s)
        ms[-1] = len(s) - 1
        for i in range(len(s)-2,-1,-1):
            if s[i] > s[ms[i+1]]:
                ms[i] = i
            else:
                ms[i] = ms[i+1]
        
        print(ms)
        
        ls = list(s)
        for i in range(len(s)):
            if ms[i] != i and ls[ms[i]] != ls[i]:
                ls[i], ls[ms[i]] = ls[ms[i]], ls[i]
                break
        return int(''.join(ls))          
