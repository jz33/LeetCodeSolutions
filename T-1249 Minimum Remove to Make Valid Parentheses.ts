/*
1249. Minimum Remove to Make Valid Parentheses
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')',
in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

    It is the empty string, contains only lowercase characters, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.

Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"

Constraints:

    1 <= s.length <= 105
    s[i] is either'(' , ')', or lowercase English letter.

*/
function minRemoveToMakeValid(s: string): string {
    // Record indexes of invalid right brackets who has no matching left brackets
    const rightBrackets: number[] = [];
    // Record indexes of left brackets. The leftover left brackets are invalid
    const leftBrackets: number[] = [];
    for (let i = 0; i < s.length; i++) {
        const char = s[i];
        if (char === '(') {
            leftBrackets.push(i);
        } else if (char === ')') {
            if (!leftBrackets.length) {
                rightBrackets.push(i);
            } else {
                leftBrackets.pop();
            }
        }
    }
    // Re-construct the string without the indexes saved in left / right stacks
    const newChars: string[] = [];
    let iLeft = 0;
    let iRight = 0;
    for (let i = 0; i < s.length; i++) {
        if (iLeft < leftBrackets.length && leftBrackets[iLeft] === i) {
            iLeft++;
        } else if (iRight < rightBrackets.length && rightBrackets[iRight] === i) {
            iRight++;
        } else {
            newChars.push(s[i]);
        }
    }
    return newChars.join('');
};

