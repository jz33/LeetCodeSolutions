''
856. Score of Parentheses
https://leetcode.com/problems/score-of-parentheses/

Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

    "()" has score 1.
    AB has score A + B, where A and B are balanced parentheses strings.
    (A) has score 2 * A, where A is a balanced parentheses string.

Example 1:

Input: s = "()"
Output: 1

Example 2:

Input: s = "(())"
Output: 2

Example 3:

Input: s = "()()"
Output: 2

Constraints:
    2 <= s.length <= 50
    s consists of only '(' and ')'.
    s is a balanced parentheses string.
'''
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        scores = [0]
        for c in s:
            if c == '(':
                scores.append(0)
            else:
                lastScore = scores.pop()
                # If last is a (, score 1;
                # Otherwise, there is already at least a closed pair, score double
                score = 1 if lastScore == 0 else lastScore * 2
                # Incremently update stack[-1] to simulate +
                scores[-1] += score
        return scores[0]
