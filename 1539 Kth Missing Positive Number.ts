/*
1539. Kth Missing Positive Number
https://leetcode.com/problems/kth-missing-positive-number/

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Return the kth positive integer that is missing from this array.

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.

Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing positive integer is 6.

Constraints:
    1 <= arr.length <= 1000
    1 <= arr[i] <= 1000
    1 <= k <= 1000
    arr[i] < arr[j] for 1 <= i < j <= arr.length
Follow up:

Could you solve this problem in less than O(n) complexity?
*/
function findKthPositive(nums: number[], k: number): number {
    // Similar idea to 1060. Missing Element in Sorted Array
    let upperBound: number | null = null;
    let left = 0;
    let right = nums.length - 1;
    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        const missingCountOnLeft = nums[mid] - mid - 1;
        if (missingCountOnLeft < k) {
            upperBound = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    if (upperBound === null) {
        return k;
    } else {
        const missingCountOnLeft = nums[upperBound] - upperBound - 1;
        return k - missingCountOnLeft + nums[upperBound];
    }
}
