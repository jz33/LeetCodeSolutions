/*
1358. Number of Substrings Containing All Three Characters
https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.


Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

Example 3:

Input: s = "abc"
Output: 1

Constraints:
    3 <= s.length <= 5 x 10^4
    s only consists of a, b or c characters.
*/

function numberOfSubstrings(s: string): number {
    // Sliding Window
    let left = 0;
    let right = 0;
    const counter = new Map<string, number>([
        ['a', 0],
        ['b', 0],
        ['c', 0],
    ]);

    const isValid = (): boolean =>
        !!counter.get('a') && !!counter.get('b') && !!counter.get('c');

    let validCount = 0;
    while (left < s.length) {
        // Extend
        while (right < s.length && !isValid()) {
            const char = s[right];
            counter.set(char, counter.get(char)! + 1);
            right++;
        }
        if (isValid()) {
            // If a substring [left: right] is valid,
            // all substrings of [left:right], [left: right+1],... are valid
            validCount += s.length - right + 1;
        }
        // Shrink
        const leftChar = s[left];
        counter.set(leftChar, counter.get(leftChar)! - 1);
        left++;
    }

    return validCount;
}
