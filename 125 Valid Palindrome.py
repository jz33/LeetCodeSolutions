'''
125. Valid Palindrome
https://leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:

Input: "race a car"
Output: false
'''
class Solution:
    '''
    Re-trim + string comparison, faster
    '''
    def isPalindrome(self, s: str) -> bool:
        trimmed = re.sub("\W", "", s).lower()
        size = len(trimmed)
        halfSize = (size >> 1)
        if (size & 1) == 1:
            return trimmed[:halfSize] == trimmed[:halfSize:-1]
        else:
            return trimmed[:halfSize] == trimmed[:halfSize-1:-1]
        
class Solution:
    '''
    Two Pointers, slower
    '''
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1
        return True
