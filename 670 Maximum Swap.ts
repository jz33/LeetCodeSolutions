/*
670. Maximum Swap
https://leetcode.com/problems/maximum-swap/

You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.

Constraints:
    0 <= num <= 108

The given number is in the range [0, 108]
*/

function maximumSwap(num: number): number {
    const digits: string[] = `${num}`.split('');

    // The maxIndexes[i] saves the index on digitList who has maximum value in digitList[i:]
    const maxIndexes = new Array(digits.length);
    maxIndexes[digits.length - 1] = digits.length - 1;
    for (let i = digits.length - 2; i >= 0; i--) {
        if (digits[i] > digits[maxIndexes[i + 1]]) {
            maxIndexes[i] = i;
        } else {
            maxIndexes[i] = maxIndexes[i + 1];
        }
    }

    // From left to right, swap if there is a larger digit on right
    for (let i = 0; i < digits.length; i++) {
        const k = maxIndexes[i];
        if (k !== i && digits[k] !== digits[i]) {
            [digits[i], digits[k]] = [digits[k], digits[i]];
            break;
        }
    }

    return parseInt(digits.join(''));
}      
