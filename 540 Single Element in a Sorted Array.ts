/*
540. Single Element in a Sorted Array
https://leetcode.com/problems/single-element-in-a-sorted-array/

You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10

Constraints:

    1 <= nums.length <= 105
    0 <= nums[i] <= 105
*/

function singleNonDuplicate(nums: number[]): number {
    /*
    If the array has all numbers appears twice (aka, no single number),
    then all even index e in range, it has nums[e] = nums[e+1].
    And the single number can only appear in an even index.
    So, if nums[e] = nums[e+1], the single number should appear in right branch;
    vice verse, if nums[e] != nums[e+1], the single number should appear in left branch.
    */
    let left = 0;
    let right = nums.length - 1;
    while (left < right) {
        const mid = (left + right) / 2;
        const midEven = mid % 2 === 0 ? mid : mid - 1;
        if (nums[midEven] === nums[midEven + 1]) {
            // The single number is num[midEven+2] or right
            left = midEven + 2;
        } else {
            // The single number is num[midEven] or left
            right = midEven;
        }
    }
    // It must left == right, so either nums[left] or nums[right]
    return nums[right];
}
