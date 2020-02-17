'''
1055. Shortest Way to Form String
https://leetcode.com/problems/shortest-way-to-form-string/

From any string, we can form a subsequence of that string by deleting some number of characters (possibly no deletions).

Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals
target. If the task is impossible, return -1.

Example 1:

Input: source = "abc", target = "abcbc"
Output: 2
Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".

Example 2:

Input: source = "abc", target = "acdbc"
Output: -1
Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.

Example 3:

Input: source = "xyz", target = "xzyxz"
Output: 3
Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
 

Constraints:

Both the source and target strings consist of only lowercase English letters from "a"-"z".
The lengths of source and target string are between 1 and 1000.
'''
from copy import deepcopy

class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        '''
        O(M+N) method
        '''
        # Preprocesing: build the index map on source.
        # dp[i] is a {char : index} dict where index is the 
        # closest index of char which appears on i or later than i
        sourceSize = len(source)
        dp = [None] * sourceSize
        dp[-1] = {source[-1] : sourceSize - 1}
        for i in range(sourceSize-2, -1, -1):
            dp[i] = deepcopy(dp[i+1])
            dp[i][source[i]] = i
            
        i = sourceSize # iterater for dp (aka, source)
        cycleCount = 0
        for t in target:
            # No appearance of t in source[i:],
            # or i is at sourceSize, 
            # reset i to 0
            if i == sourceSize or t not in dp[i]:
                i = 0
                cycleCount += 1
                
            togo = dp[i].get(t)
            if togo is None:
                return -1
            
            i = togo + 1         
        return cycleCount          
