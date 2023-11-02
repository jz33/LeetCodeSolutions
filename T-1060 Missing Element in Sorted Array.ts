/*
1060. Missing Element in Sorted Array
https://leetcode.com/problems/missing-element-in-sorted-array/

Given an integer array nums which is sorted in ascending order and all of its elements are unique and given also an integer k, return the kth missing number starting from the leftmost number of the array.

Example 1:

Input: nums = [4,7,9,10], k = 1
Output: 5
Explanation: The first missing number is 5.

Example 2:

Input: nums = [4,7,9,10], k = 3
Output: 8
Explanation: The missing numbers are [5,6,8,...], hence the third missing number is 8.

Example 3:

Input: nums = [1,2,4], k = 3
Output: 6
Explanation: The missing numbers are [3,5,6,7,...], hence the third missing number is 6.

Constraints:
    1 <= nums.length <= 5 * 104
    1 <= nums[i] <= 107
    nums is sorted in ascending order, and all the elements are unique.
    1 <= k <= 108
*/
function missingElement(nums: number[], k: number): number {
    // Observation:
    // On index i, the count of missing numbers on its left (exclusive)
    // is: nums[i] - i - nums[0]
    // On i, if left missing number count >=k, then kth missing number is on i's left;
    // otherwise, kth missing number is on i's right
    // So, the key is to find the index i which is the largest index that has
    // left  missing numbers count < K
    let upperBound = 0;
    let left = 0;
    let right = nums.length - 1;
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        const missingCountOnLeft = nums[mid] - mid - nums[0];
        if (missingCountOnLeft < k ) {
            upperBound = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    const missingCountOnLeft = nums[upperBound] - upperBound - nums[0];
    return k - missingCountOnLeft + nums[upperBound];
};
