/*
1492. The kth Factor of n
https://leetcode.com/problems/the-kth-factor-of-n/

You are given two positive integers n and k. A factor of an integer n is defined as an integer i where n % i == 0.

Consider a list of all factors of n sorted in ascending order, return the kth factor in this list or return -1 if n has less than k factors.

Example 1:

Input: n = 12, k = 3
Output: 3
Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.

Example 2:

Input: n = 7, k = 2
Output: 7
Explanation: Factors list is [1, 7], the 2nd factor is 7.

Example 3:

Input: n = 4, k = 4
Output: -1
Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.

Constraints:
    1 <= k <= n <= 1000
*/
function kthFactor(n: number, k: number): number {
    const root = Math.sqrt(n);
    const rootInt = Math.floor(root);
    let halfFactorCount = 0;
    for (let i = 1; i <= rootInt; i++) {
        if (n % i === 0) {
            halfFactorCount++;
            if (halfFactorCount === k) {
                return i;
            }
        }
    }
    const isPerfectSquare = root === rootInt;
    const totalFactorCount = isPerfectSquare
        ? halfFactorCount * 2 - 1
        : halfFactorCount * 2;
    if (totalFactorCount < k) {
        return -1;
    }
    // Iterate from 1 again, which will be faster than from back.
    // Determine the next run's depth
    const reverseK = isPerfectSquare
        ? halfFactorCount - (k - halfFactorCount)
        : halfFactorCount - (k - halfFactorCount) + 1;
    let reverseFactorCount = 0;
    for (let i = 1; i <= rootInt; i++) {
        if (n % i === 0) {
            reverseFactorCount++;
            if (reverseFactorCount === reverseK) {
                return n / i;
            }
        }
    }
    return -1;
}
