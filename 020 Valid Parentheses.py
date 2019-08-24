'''
20 Valid Parentheses
https://oj.leetcode.com/problems/valid-parentheses/
'''
class Solution:
    def isValid(self, s: str) -> bool:
        lefts = ['(', '[', '{'] # left parts of parentheses
        
        def rightToLeft(s: str) -> str:
            if s == ')':
                return '('
            elif s == ']':
                return '['
            elif s == '}':
                return '{'
        
        buf = []
        for c in s:
            if c in lefts:
                buf.append(c)
            else:
                if len(buf) == 0 or buf[-1] != rightToLeft(c):
                    return False
                buf.pop()
                
        return len(buf) == 0
