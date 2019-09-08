/*
Missing Number
https://leetcode.com/problems/missing-number/
*/
/**
 * @param {number[]} nums
 * @return {number}
 */
/*
Let's say the numbers are 0,1,2,...L
Obviously (regardless of xor order):
    0^0^1^1^2^2^...^L^L = 0
Assume M is missing, then (regardless of xor order):
    0^0^1^1^2^2^...^M^M^...^L^L = 0
Xor M on both side:
    0^0^1^1^2^2^...^M^...^L^L = M
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
