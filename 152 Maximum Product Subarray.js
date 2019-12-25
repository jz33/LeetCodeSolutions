/*
152. Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray

Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
*/
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    if (nums.length === 0) {
        return 0;
    }
    
    var maxVal = nums[0];
    var minVal = nums[0];
    var res = nums[0];
    
    var nextMaxVal, nextMinVal;
    nums.forEach(function(v, i) {
        if(i > 0) {
            nextMaxVal = Math.max(v, v * maxVal, v * minVal);
            nextMinVal = Math.min(v, v * maxVal, v * minVal);
            maxVal = nextMaxVal;
            minVal = nextMinVal;
            res = Math.max(res, maxVal);
        }
    });
    
    return res;
};
