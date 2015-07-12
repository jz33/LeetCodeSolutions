/*
House Robber
https://leetcode.com/problems/house-robber/
*/
/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    var arrayLength = nums.length;
    
    if(arrayLength === 0) return 0;
    if(arrayLength === 1) return nums[0];
    if(arrayLength === 2) return Math.max(nums[0],nums[1]);
    
    var three_steps = nums[0]; // max at i - 3
    var two_steps = Math.max(nums[0],nums[1]); // max at i - 2
    var one_step = Math.max(nums[0]+nums[2],nums[1]); // max at i - 1
    
    // max at i = 2
    var maxIncome = one_step;
    
    for (var i = 3; i < arrayLength; i++) {
        maxIncome = Math.max(maxIncome, Math.max(three_steps,two_steps) + nums[i]);
        three_steps = two_steps;
        two_steps = one_step;
        one_step = maxIncome;
    }
    
    return maxIncome;
};

var r = 0
var arr = new Array(2,7,9,3,1)
r = rob(arr)
console.log(r);
