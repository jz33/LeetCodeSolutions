'''
844. Backspace String Compare
https://leetcode.com/problems/backspace-string-compare/

Given two strings S and T, return if they are equal when both are typed into empty text editors.
# means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
'''
class Solution:
    def getFinal(self, s: str):
        stack = []
        for e in s:
            if e == '#':
                if stack:
                    stack.pop()
            else:
                stack.append(e)
        return ''.join(stack)
    
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.getFinal(S) == self.getFinal(T)
