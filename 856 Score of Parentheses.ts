/*
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
*/
function scoreOfParentheses(s: string): number {
    // The stack saves previous scores.
    // A score is only saved when encountering ')'
    // Set stack[0] for convenience of poping and score accumulating.
    const stack: number[] = [0];
    for (const char of s) {
        if (char === '(') {
            stack.push(0);
        } else {
            const last = stack.pop();
            // If last is a (, score 1;
            // Otherwise, there is already at least a closed pair, score double
            const score = last === 0 ? 1 : last * 2;
            stack[stack.length - 1] += score;
        }
    }
    return stack[0];
};
