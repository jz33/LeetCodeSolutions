"use strict";
/*
Range Sum Query - Immutable
https://leetcode.com/problems/range-sum-query-immutable/
*//**
 * @constructor
 * @param {number[]} nums
 */
var NumArray = function(nums) {
    var length = nums.length;
    var arr = [];
    arr[-1] = 0;
    for(var i = 0;i<length;i++){
       arr[i] = arr[i-1] + nums[i];
    }
    this.arr = arr;
};

/**
 * @param {number} i
 * @param {number} j
 * @return {number}
 */
NumArray.prototype.sumRange = function(i, j) {
    return this.arr[j] - this.arr[i-1];
}

var nums = [-2,0,3,-5,2,-1];
var obj = new NumArray(nums);
console.log(obj.sumRange(0,2))
console.log(obj.sumRange(2,5))
console.log(obj.sumRange(0,5))
