/*
78. Subsets
https://leetcode.com/problems/subsets/

Given an integer array nums of unique elements, return all possible
subsets
(the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

Example 2:

Input: nums = [0]
Output: [[],[0]]

Constraints:

    1 <= nums.length <= 10
    -10 <= nums[i] <= 10
    All the numbers of nums are unique.
*/
function subsets(nums: number[]): number[][] {
    // Total number is the nums.length ^ 2
    const total = 1 << nums.length;
    const result: number[][] = [];
    for (let t = 0; t < total; t++) {
        // Check each bit of t, if is '1', then select nums[i]
        const row: number[] = [];
        for (let c = 0; c < nums.length; c++) {
            const checker = 1 << c;
            if (checker > t) {
                // If checker > t, no more '1's on left
                break;
            }
            if (checker & t) {
                row.push(nums[c]);
            }
        }
        result.push(row);
    }
    return result;
};
