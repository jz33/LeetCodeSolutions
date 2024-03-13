'''
32. Longest Valid Parentheses
https://leetcode.com/problems/longest-valid-parentheses

Given a string containing just the characters '(' and ')',
return the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".

Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".

Example 3:

Input: s = ""
Output: 0

Constraints:
    0 <= s.length <= 3 * 104
    s[i] is '(', or ')'
'''
def oneDirection(source: str, leftBracket: str) -> int:
    '''
    In left to right order, @leftBracket is '('
    In reversed order, @leftBracket is ')'
    '''
    longest = 0
    start = 0
    leftCount = 0
    for i, c in enumerate(source):
        if c == leftBracket:
            leftCount += 1
        else:
            leftCount -= 1
    
        if leftCount == 0:
            # Notice do not reset "start" here
            longest = max(longest, i - start + 1)             
        elif leftCount < 0:
            # Reset
            leftCount = 0
            start = i + 1
    return longest
    
class Solution:
    def longestValidParentheses(self, source: str) -> int:        
        return max(oneDirection(source, '('), oneDirection(source[::-1], ')'))
