/*
1541. Minimum Insertions to Balance a Parentheses String
https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/

Given a parentheses string s containing only the characters '(' and ')'. A parentheses string is balanced if:

    Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
    Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.

In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.

    For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" are not balanced.

You can insert the characters '(' and ')' at any position of the string to balance it if needed.

Return the minimum number of insertions needed to make s balanced.

Example 1:

Input: s = "(()))"
Output: 1
Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching.
We need to add one more ')' at the end of the string to be "(())))" which is balanced.

Example 2:

Input: s = "())"
Output: 0
Explanation: The string is already balanced.

Example 3:

Input: s = "))())("
Output: 3
Explanation: Add '(' to match the first '))', Add '))' to match the last '('.

Constraints:
    1 <= s.length <= 105
    s consists of '(' and ')' only.
*/
function minInsertions(s: string): number {
    let leftBrackets: number = 0;
    let needed: number = 0;
    let i = 0; // iterator of s
    while (i < s.length) {
        if (s[i] === '(') {
            leftBrackets++;
            i++;
        } else if (s[i] === ')') {
            // ))
            if (i + 1 < s.length && s[i + 1] === ')') {
                if (leftBrackets > 0) {
                    // Balanced
                    leftBrackets--;
                } else {
                    // Need 1 (
                    needed++;
                }
                i += 2;
            } else { // )( or )[end]
                if (leftBrackets > 0) {
                    // Need 1 )
                    leftBrackets--;
                    needed++;
                } else {
                    // Need 1 (, 1 )
                    needed += 2;
                }
                i++;
            }
        }
    }
    // All leftover ( needs ))
    return leftBrackets * 2 + needed;
};
