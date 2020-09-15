/*
233. Number of Digit One
https://leetcode.com/problems/number-of-digit-one/

Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Example:

Input: 13
Output: 6 
Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
*/
/**
 * Count how many '1's in a number with width of @wid
 * 1: 9: 1
 * 2: 99: 20
 * 3: 999: 300
 * 4: 9999: 4000
 * @param wid: [1, 9]
 */
function countOneWidth(wid: number): number {
    return wid * (10 ** (wid - 1))
}

/**
 * Consider this function is 'f', input is string 's',
 * the idea is compute '1's at s[0] + f[s[1:]]
 * 1. s is 0*: easily, nothing gain in s[0], so result is subroutine, f[s[1:]]
 * 2. s is 1*: 3 parts:
 *     a. Count '1's of 1*, but only the '1's at s[0], this is int(s[1:]) + 1
 *     b. Count '1's of 1*, but only the '1's at s[1:], this goes to subroutine
 *     c. Count '1's of 99...9 (length = s.length - 1), use countOneWidth
 * 3. s is [2-9]: 3 parts:
 *     a. Count '1's of 1*, this is 10 * s[1:].length
 *     b. Count '1's of s[0]*, but only the '1's at s[1:], this goes to subroutine
 *     c. Count '1's of 99...9 (length = s.length - 1), use countOneWidth. There are int(s) like this.
 * 			
 * @param s: use string represetation to get left-most digit quicker
 */
function countOne(s: string): number {
    if (!s) {
        return 0
    }

    let w: number = s.length - 1
    let c: string = s[0]
    let r: string = s.substring(1)
    if (c === '0') {
        return countOne(r)
    }
    else if (c === '1') {
        return (+r) + 1 + countOneWidth(w) + countOne(r)
    }
    else {
        return 10 ** w + (+c) * countOneWidth(w) + countOne(r)
    }
}

function countDigitOne(n: number): number {
    if (n <= 0) {
        return 0
    }
    return countOne(n.toString())
};
