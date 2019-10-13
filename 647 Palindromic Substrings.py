'''
647. Palindromic Substrings
https://leetcode.com/problems/palindromic-substrings/

Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted as different substrings even
they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
'''
class Solution:
    '''
    Same method as 5. Longest Palindromic Substring
    '''
    def extend(self, s: str, i: int, j: int) -> int:
        res = 0
        while i > -1 and j < len(s) and s[i] == s[j]:
            res += 1
            i -= 1
            j += 1
        return res
    
    def countSubstrings(self, s: str) -> int:
        res = 0
        # Expand from center
        for i in range(len(s)):
            res += self.extend(s,i,i)
            res += self.extend(s,i,i+1)
        return res
