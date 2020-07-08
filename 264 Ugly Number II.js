/*
264. Ugly Number II
https://leetcode.com/problems/ugly-number-ii/

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

Note:  

1 is typically treated as an ugly number.
n does not exceed 1690.
*/
var uglies = [1]; // holding all ugly numbers
var p2 = 0; // Latest factored by 2 number
var p3 = 0; // Latest factored by 3 number
var p5 = 0; // Latest factored by 5 number

/**
 * @param {number} n
 * @return {number}
 */
var nthUglyNumber = function(n) {
    // Notice i does not start from 1
    // Some ugly numbers can be already calculated in previous runs
    var i = uglies.length;
    for (;i < n ;++i) {
        var r2 = uglies[p2] * 2;
        var r3 = uglies[p3] * 3;
        var r5 = uglies[p5] * 5;
        var m = Math.min(r2,r3,r5);
        if (m === r2) {
            p2++;
        }
        if (m === r3) {
            p3++;
        }
        if (m === r5) {
            p5++;
        }
        uglies[i] = m;
    }
    return uglies[n-1]; 
};
