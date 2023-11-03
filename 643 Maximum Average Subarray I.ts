/*
643. Maximum Average Subarray I
https://leetcode.com/problems/maximum-average-subarray-i/

You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
Any answer with a calculation error less than 10-5 will be accepted.

Example 1:

Input: nums = [1,12,-5,-6,50,3], k = 4
Output: 12.75000
Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

Example 2:

Input: nums = [5], k = 1
Output: 5.00000
*/
function findMaxAverage(nums: number[], width: number): number {
    let total = nums.slice(0, width).reduce((prev, curr) => prev + curr, 0);
    let maxAvg = total / width;
    for (let i = 0; i < nums.length - width; i++) {
        total = total - nums[i] + nums[i + width];
        maxAvg = Math.max(maxAvg, total / width);
    }
    return maxAvg;
}
