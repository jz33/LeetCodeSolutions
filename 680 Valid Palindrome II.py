'''
680. Valid Palindrome II
https://leetcode.com/problems/valid-palindrome-ii

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true

Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:

Input: s = "abc"
Output: false

Constraints:
    1 <= s.length <= 105
    s consists of lowercase English letters.
'''
def isPalindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) -1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # Delete either left or right
                return isPalindrome(s[left : right]) or isPalindrome(s[left + 1: right + 1])
        return True