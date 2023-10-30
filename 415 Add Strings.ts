/*
415. Add Strings
https://leetcode.com/problems/add-strings/

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"

Constraints:

    1 <= num1.length, num2.length <= 104
    num1 and num2 consist of only digits.
    num1 and num2 don't have any leading zeros except for the zero itself.
*/
function addStrings(num1: string, num2: string): string {
    const list1: number[] = num1.split('').map((char) => parseInt(char));
    const list2: number[] = num2.split('').map((char) => parseInt(char));
    let i1 = list1.length - 1;
    let i2 = list2.length - 1;
    let accumulation = 0;
    let total = 0;
    const result: number[] = [];

    const compute = (v1: number | null, v2: number | null) => {
        total = (v1 ?? 0) + (v2 ?? 0) + accumulation;
        if (total > 9) {
            accumulation = 1;
            total -= 10;
        } else {
            accumulation = 0;
        }
        result.push(total);
        if (v1 !== null) {
            i1--;
        }
        if (v2 !== null) {
            i2--;
        }
    };

    while (i1 >= 0 && i2 >= 0) {
        compute(list1[i1], list2[i2]);
    }
    while (i1 >= 0) {
        compute(list1[i1], null);
    }
    while (i2 >= 0) {
        compute(null, list2[i2]);
    }
    if (accumulation) {
        compute(null, null);
    }
    return result.reverse().join('');
}
