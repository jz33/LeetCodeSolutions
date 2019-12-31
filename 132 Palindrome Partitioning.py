'''
132. Palindrome Partitioning II
https://leetcode.com/problems/palindrome-partitioning-ii/

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''
class Solution:
    def minCut(self, s: str) -> int:
        if s == s[::-1]:
            return 0
        
        n = len(s)
        
        # cuts[i] is minimum number of cuts for s[:i]
        # cuts[0] = -1 is for out of bound case
        cuts = list(range(-1, n))
        
        for i in range(n):
            # As center is in i, try expand to left and right to find
            # valid palindroms, then update dp on right most position (y)
            x, y = i, i
            while x > -1 and y < n and s[x] == s[y]:
                cuts[y+1] = min(cuts[y+1], cuts[x] + 1) # cuts has offset 1
                x, y = x - 1, y + 1

            x, y = i, i + 1
            while x > -1 and y < n and s[x] == s[y]:
                cuts[y+1] = min(cuts[y+1], cuts[x] + 1)
                x, y = x - 1, y + 1
                
        return cuts[-1]
