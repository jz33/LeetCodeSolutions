'''
20 Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true

Example 2:

Input: "()[]{}"
Output: true

Example 3:

Input: "(]"
Output: false

Example 4:

Input: "([)]"
Output: false

Example 5:

Input: "{[]}"
Output: true
'''
class Solution:
    def isValid(self, s: str) -> bool:
        leftParentheses = ['(', '[', '{']
        
        def arePaired(left: str, right: str) -> bool:
            if left == '(':
                return right == ')'
            elif left == '[':
                return right == ']'
            elif left == '{':
                return right == '}'
        
        stack = []
        for c in s:
            if c in leftParentheses:
                stack.append(c)
            else:
                if not stack or not arePaired(stack[-1], c):
                    return False
                stack.pop()
                
        return not stack
