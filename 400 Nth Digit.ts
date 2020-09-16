/*
400. Nth Digit
https://leetcode.com/problems/nth-digit/discuss/88363/Java-solution

Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...

Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).

Example 1:

Input:
3

Output:
3

Example 2:

Input:
11

Output:
0

Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0, which is part of the number 10.
*/
function findNthDigit(n: number): number {
    let bound: number = n - 1
    let width: number = 1
	let start: number = 1

    while (bound >= width * start * 9) {
        bound -= width * start * 9
        width++;
        start *= 10
    }

    start += Math.floor(bound / width)
    return +start.toString()[bound % width]
}
