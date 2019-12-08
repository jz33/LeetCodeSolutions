'''
316. Remove Duplicate Letters
https://leetcode.com/problems/remove-duplicate-letters/

Given a string which contains only lowercase letters,
remove duplicate letters so that every letter appears once and only once.
You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"
Example 2:

Input: "cbacdcbc"
Output: "acdb"
'''
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        ctr = collections.Counter(s)
        stack = []
        for c in s:
            if c not in stack:
                while stack and stack[-1] > c and ctr[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            ctr[c] -= 1
        return ''.join(stack)
