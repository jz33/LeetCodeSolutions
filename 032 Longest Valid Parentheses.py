'''
32 Longest Valid Parentheses
https://leetcode.com/problems/longest-valid-parentheses/description/

Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''
class Solution:
    def OneDirection(self, src: str, leftBracket: str) -> int:
        '''
        In left to right order, @leftBracket is '('
        In reversed order, @leftBracket is ')'
        '''
        longest = 0
        start = 0
        brackets = 0
        for i, c in enumerate(src):
            if c == leftBracket:
                brackets += 1
            else:
                brackets -= 1
        
            if brackets == 0:
                # Notice do not reset "start" here
                longest = max(longest, i - start + 1)             
            elif brackets < 0:
                # Reset
                brackets = 0
                start = i + 1

        return longest
        
    def longestValidParentheses(self, src: str) -> int:        
        return max(self.OneDirection(src, '('), self.OneDirection(src[::-1], ')'))
