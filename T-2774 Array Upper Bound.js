/*
2774. Array Upper Bound
https://leetcode.com/problems/array-upper-bound/

Write code that enhances all arrays such that you can call the upperBound() method on any array and
it will return the last index of a given target number.
nums is a sorted ascending array of numbers that may contain duplicates.
If the target number is not found in the array, return -1.

Example 1:

Input: nums = [3,4,5], target = 5
Output: 2
Explanation: Last index of target value is 2

Example 2:

Input: nums = [1,4,5], target = 2
Output: -1
Explanation: Because there is no digit 2 in the array, return -1.

Example 3:

Input: nums = [3,4,6,6,6,6,7], target = 6
Output: 5
Explanation: Last index of target value is 5

Constraints:
    1 <= nums.length <= 104
    -104 <= nums[i], target <= 104
    nums is sorted in ascending order.
*/
/** 
 * @param {number} target
 * @return {number}
 */
Array.prototype.upperBound = function(target) {
    var left = 0;
    var right = this.length - 1;
    var bound = null;
    while (left <= right) {
        const mid = (left + right) >> 1;
        const midVal = this[mid];
        if (midVal < target) {
            left = mid + 1;
        } else if (midVal === target) {
            bound = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return bound === null ? - 1 : bound;
};
