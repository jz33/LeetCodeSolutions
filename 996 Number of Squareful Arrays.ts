/*
996. Number of Squareful Arrays
https://leetcode.com/problems/number-of-squareful-arrays/

An array is squareful if the sum of every pair of adjacent elements is a perfect square.

Given an integer array nums, return the number of permutations of nums that are squareful.

Two permutations perm1 and perm2 are different if there is some index i such that perm1[i] != perm2[i].

Example 1:

Input: nums = [1,17,8]
Output: 2
Explanation: [1,8,17] and [17,8,1] are the valid permutations.

Example 2:

Input: nums = [2,2,2]
Output: 1

Constraints:

    1 <= nums.length <= 12
    0 <= nums[i] <= 109

*/
const isSquare = (a: number): boolean => {
    const root = Math.floor(Math.sqrt(a));
    return root * root === a;
};
/**
 * Based on 47. Permutations II
 */
function numSquarefulPerms(nums: number[]): number {
    const size = nums.length;
    let permsCount = 0;

    const topDown = (arr: number[], start: number): void => {
        // Unlike Permutations II, not start === size - 1,
        // as we want to check isSquare(arr[size - 2] + arr[size - 1]))
        if (start === size) { 
            permsCount++;
            console.log(arr);
        } else {
            for (let i = start; i < size; i++) {
                if (i !== start && arr[i] === arr[start]) {
                    continue;
                }
                [arr[i], arr[start]] = [arr[start], arr[i]];
                if (start === 0 || isSquare(arr[start - 1] + arr[start])) {
                    topDown([...arr], start + 1);
                }
            }
        }
    };

    topDown(nums.sort(), 0);
    return permsCount;
}
