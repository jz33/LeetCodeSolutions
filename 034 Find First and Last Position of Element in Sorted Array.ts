/*
34. Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

Given an array of integers nums sorted in non-decreasing order,
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    nums is a non-decreasing array.
    -109 <= target <= 109

*/
// Same as 2089. Find Target Indices After Sorting Array
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

function searchRange(nums: number[], target: number): number[] {
    return [getLowerBound(nums, target), getUpperBound(nums, target)];
};
