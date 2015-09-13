import re
'''
Valid Palindrome
https://leetcode.com/problems/valid-palindrome/
'''
def isPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    s = re.sub("\W", "", s).lower()
    return s == s[::-1]
