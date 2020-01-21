/*
303. Range Sum Query - Immutable
https://leetcode.com/problems/range-sum-query-immutable/

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
Note:

You may assume that the array does not change.
There are many calls to sumRange function.
*/
/**
 * @param {number[]} nums
 */
var NumArray = function(nums) {
    var length = nums.length;
    var arr = [0];
    for (var i = 0;i < length; ++i) {
       arr[i+1] = arr[i] + nums[i];
    }
    this.arr = arr;
};

/** 
 * @param {number} i 
 * @param {number} j
 * @return {number}
 */
NumArray.prototype.sumRange = function(i, j) {
    return this.arr[j+1] - this.arr[i];
};
