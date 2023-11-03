/*
152. Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find a
subarray
that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:
    1 <= nums.length <= 2 * 104
    -10 <= nums[i] <= 10
    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
*/
function maxProduct(nums: number[]): number {
    // The maxValue and minValue on index i means
    // the max / min product value in subarray [:i]
    let maxValue = 1;
    let minValue = 1;
    let result = Number.MIN_SAFE_INTEGER;
    for (const value of nums) {
        [maxValue, minValue] = [
            Math.max(value, value * maxValue, value * minValue),
            Math.min(value, value * maxValue, value * minValue),
        ];
        result = Math.max(result, maxValue);
    }
    return result;
}
