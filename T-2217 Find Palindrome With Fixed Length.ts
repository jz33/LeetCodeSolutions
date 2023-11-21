/*
2217. Find Palindrome With Fixed Length
https://leetcode.com/problems/find-palindrome-with-fixed-length/

Given an integer array queries and a positive integer intLength,
return an array answer where answer[i] is either the queries[i]th smallest positive palindrome of length intLength
or -1 if no such palindrome exists.

A palindrome is a number that reads the same backwards and forwards. Palindromes cannot have leading zeros.

Example 1:

Input: queries = [1,2,3,4,5,90], intLength = 3
Output: [101,111,121,131,141,999]
Explanation:
The first few palindromes of length 3 are:
101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, ...
The 90th palindrome of length 3 is 999.

Example 2:

Input: queries = [2,4,6], intLength = 4
Output: [1111,1331,1551]
Explanation:
The first six palindromes of length 4 are:
1001, 1111, 1221, 1331, 1441, and 1551.

Constraints:
    1 <= queries.length <= 5 * 104
    1 <= queries[i] <= 109
    1 <= intLength <= 15
*/
function oddCase(queries: number[], intLength: number): number[] {
    const halfSize = (intLength + 1) / 2; // 5 -> 3
    const lowerBound = Math.pow(10, halfSize - 1);
    const upperBound = Math.pow(10, halfSize) - 1;
    const count = upperBound - lowerBound + 1;
    return queries.map(query => {
        if (query > count) {
            return -1;
        }
        const half = `${lowerBound + query - 1}`;
        const halfWithoutMiddle = half.substring(0, half.length - 1);
        const reversedHalfWithoutMiddle = halfWithoutMiddle.split('').reverse().join('');
        return parseInt(halfWithoutMiddle + half.at(-1) + reversedHalfWithoutMiddle);
    });
}

function evenCase(queries: number[], intLength: number): number[] {
    const halfSize = intLength / 2;
    const lowerBound = Math.pow(10, halfSize - 1);
    const upperBound = Math.pow(10, halfSize) - 1;
    const count = upperBound - lowerBound + 1;
    return queries.map(query => {
        if (query > count) {
            return -1;
        }
        const half = `${lowerBound + query - 1}`;
        const reversedHalf = half.split('').reverse().join('');
        return parseInt(half + reversedHalf);
    });
}

function kthPalindrome(queries: number[], intLength: number): number[] {
    if (intLength % 2 === 0) {
        return evenCase(queries, intLength);
    } else {
        return oddCase(queries, intLength);
    }
};
