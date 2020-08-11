'''
678. Valid Parenthesis String
https://leetcode.com/problems/valid-parenthesis-string/

Given a string containing only three types of characters: '(', ')' and '*',
write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.

Example 1:
Input: "()"
Output: True

Example 2:
Input: "(*)"
Output: True

Example 3:
Input: "(*))"
Output: True
Note:
The string size will be in the range [1, 100].
'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        minLeftCount = 0 # Count only '(' as left parenthesis
        maxLeftCount = 0 # Count both '(' and '*' as left parenthesis
        
        for c in s:
            if c == '(':
                minLeftCount += 1
                maxLeftCount += 1
            elif c == ')':
                minLeftCount -= 1
                maxLeftCount -= 1
            else: # c == '*'
                minLeftCount -= 1
                maxLeftCount += 1
            
            # If anytime '(' + '*' is less than ')', invalid
            if maxLeftCount < 0:
                return False
            
            # If left is exhausted, convert a '*' to '('
            minLeftCount = max(minLeftCount, 0)
        
        # There should not be outstanding '('
        return minLeftCount == 0
