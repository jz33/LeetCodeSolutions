/*
2089. Find Target Indices After Sorting Array
https://leetcode.com/problems/find-target-indices-after-sorting-array/

You are given a 0-indexed integer array nums and a target element target.

A target index is an index i such that nums[i] == target.

Return a list of the target indices of nums after sorting nums in non-decreasing order.
If there are no target indices, return an empty list. The returned list must be sorted in increasing order.

Example 1:

Input: nums = [1,2,5,2,3], target = 2
Output: [1,2]
Explanation: After sorting, nums is [1,2,2,3,5].
The indices where nums[i] == 2 are 1 and 2.

Example 2:

Input: nums = [1,2,5,2,3], target = 3
Output: [3]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 3 is 3.

Example 3:

Input: nums = [1,2,5,2,3], target = 5
Output: [4]
Explanation: After sorting, nums is [1,2,2,3,5].
The index where nums[i] == 5 is 4.

Constraints:
    1 <= nums.length <= 100
    1 <= nums[i], target <= 100
*/
/**
 * Get the first appearance index of target in nums.
 * If target is not in nums, return -1
 */
function getLowerBound(nums: number[], target: number): number {
    let left = 0;
    let right = nums.length - 1;
    let bound: number | null = null;
    while (left <= right) {
        const mid = (left + right) >> 1;
        const midVal = nums[mid];
        if (midVal < target) {
            left = mid + 1;
        } else if (midVal === target) {
            bound = mid;
            right = mid - 1;
        } else {
            right = mid - 1;
        }
    }
    return bound === null ? -1 : bound;
}

/**
 * Get the last appearance index of target in nums.
 * If target is not in nums, return -1
 * Same as 2774. Array Upper Bound
 */
function getUpperBound(nums: number[], target: number): number {
    let left = 0;
    let right = nums.length - 1;
    let bound: number | null = null;
    while (left <= right) {
        const mid = (left + right) >> 1;
        const midVal = nums[mid];
        if (midVal < target) {
            left = mid + 1;
        } else if (midVal === target) {
            bound = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return bound === null ? -1 : bound;
}

function targetIndices(nums: number[], target: number): number[] {
    nums.sort((a, b) => a - b);
    const lowerBound = getLowerBound(nums, target);
    if (lowerBound === -1) {
        return [];
    }
    const upperBound = getUpperBound(nums, target);
    const result = new Array(upperBound - lowerBound + 1);
    for (let r = 0; r < result.length; r++) {
        result[r] = r + lowerBound;
    }
    return result;
}
