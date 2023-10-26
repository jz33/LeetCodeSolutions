/*
680. Valid Palindrome II
https://leetcode.com/problems/valid-palindrome-ii

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:

Input: s = "aba"
Output: true

Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.

Example 3:

Input: s = "abc"
Output: false

Constraints:

    1 <= s.length <= 105
    s consists of lowercase English letters.
*/
function isPalindrome(s: string): boolean {
    const size = s.length;
    const halfSize = size % 2 === 0 ? size / 2 : (size - 1) / 2;
    for (let i = 0; i < halfSize; i++) {
        if (s[i] !== s[size - 1 - i]) {
            return false;
        }
    }
    return true;
}

function validPalindrome(s: string): boolean {
    let left = 0;
    let right = s.length - 1;
    while (left < right) {
        if (s[left] === s[right]) {
            left += 1;
            right -= 1;
        } else {
            // Either exclude right or left
            return (
                isPalindrome(s.substring(left, right)) ||
                isPalindrome(s.substring(left + 1, right + 1))
            );
        }
    }
    return true;
}
