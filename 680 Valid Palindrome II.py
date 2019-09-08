import re
'''
680. Valid Palindrome II
https://leetcode.com/problems/valid-palindrome-ii/
Check whether a string is palindromic, can remove at most 1 character
'''
class Solution:
    def isPalindrome(self, s: str, lt: int, rt: int) -> bool:
        while lt < rt:
            if s[lt] != s[rt]:
                return False
            lt += 1
            rt -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        lt = 0
        rt = len(s) - 1
        while lt < rt:
            if s[lt] != s[rt]:
                return self.isPalindrome(s, lt+1, rt) or self.isPalindrome(s, lt, rt-1)
            else:
                lt += 1
                rt -= 1
        return True
