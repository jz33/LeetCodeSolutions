/*
Missing Number
https://leetcode.com/problems/missing-number/
*/
/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    var h = 0;
    for(var i = 0; i < nums.length;i++){
        h ^= nums[i];
        h ^= i;
    }
    h ^= nums.length;
    return h;
};

var nums = [3,1,0];
console.dir(missingNumber(nums));
