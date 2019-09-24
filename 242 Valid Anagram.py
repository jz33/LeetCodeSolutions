'''
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        book = [0] * 26
        A = ord('a')
        for e in s:
            code = ord(e) - A
            book[code] += 1
        
        for e in t:
            code = ord(e) - A
            if book[code] == 0:
                return False
            book[code] -= 1
            
        for code in book:
            if code != 0:
                return False
        
        return True
