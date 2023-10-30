/*
215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

Constraints:

    1 <= k <= nums.length <= 105
    -104 <= nums[i] <= 104

*/
/**
 * Partition the array with a random value, return the turing point
 * @param left: left index, inclusive
 * @param right: right index, inclusive
 */
function partition(nums: number[], left: number, right: number): number {
    const randomIndex = Math.floor(Math.random() * (right - left + 1)) + left;
    const randomValue = nums[randomIndex];
    // 1st, put random value to right
    [nums[randomIndex], nums[right]] = [nums[right], nums[randomIndex]];
    // 2nd, partition the array so that all elements left to turning point < random value
    let turningPoint = left;
    for (let i = left; i < right; i++) {
        if (nums[i] < randomValue) {
            if (i !== turningPoint) {
                [nums[i], nums[turningPoint]] = [nums[turningPoint], nums[i]];
            }
            turningPoint++;
        }
    }
    // 3nd, put back random value into turning point
    [nums[turningPoint], nums[right]] = [nums[right], nums[turningPoint]];
    return turningPoint;
}

/**
 * The iterative quick select algorithm.
 * Time complexity is O(N), as only 1 side is proceed
 * @param rank: the target rank when nums is ascending
 */
function quickselect(nums: number[], rank: number): number {
    let left = 0;
    let right = nums.length - 1;
    while (left < right) {
        const turningPoint = partition(nums, left, right);
        if (turningPoint === rank) {
            return nums[turningPoint];
        } else if (turningPoint < rank) {
            left = turningPoint + 1;
        } else {
            right = turningPoint - 1;
        }
    }
    return nums[left];
}

function findKthLargest(nums: number[], k: number): number {
    return quickselect(nums, nums.length - k);
}

