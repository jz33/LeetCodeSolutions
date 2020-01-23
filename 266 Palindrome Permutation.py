'''
266. Palindrome Permutation
https://leetcode.com/problems/palindrome-permutation/

Given a string, determine if a permutation of the string could form a palindrome.

Example 1:

Input: "code"
Output: false

Example 2:

Input: "aab"
Output: true

Example 3:

Input: "carerac"
Output: true
'''
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        histo = collections.Counter(s)
        oddy = 0
        for ctr in histo.values():
            if ctr % 2 == 1:
                oddy += 1
            if oddy > 1:
                return False
        return True
