/*
905. Sort Array By Parity
https://leetcode.com/problems/sort-array-by-parity/

Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.

Return any array that satisfies this condition.

Example 1:

Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Example 2:

Input: nums = [0]
Output: [0]

Constraints:
    1 <= nums.length <= 5000
    0 <= nums[i] <= 5000
*/
function sortArrayByParity(nums: number[]): number[] {
    let ei = 0;
    let oi = nums.length - 1;
    while (ei < oi) {
        if (nums[ei] % 2 === 0) {
            ei++;
        } else if (nums[oi] % 2 === 1) {
            oi--;
        } else {
            [nums[ei], nums[oi]] = [nums[oi], nums[ei]];
            ei++;
            oi--;
        }
    }
    return nums;
};
