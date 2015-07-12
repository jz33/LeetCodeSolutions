/*
House Robber II
https://leetcode.com/problems/house-robber-ii/
*/
/**
 * @param {number[]} nums
 * @return {number}
 */
var rob = function(nums) {
    var arrayLength = nums.length;
    var i = 0;
    
    if(arrayLength === 0) return 0;
    if(arrayLength === 1) return nums[0];
    if(arrayLength === 2) return Math.max(nums[0],nums[1]);
    if(arrayLength === 3) return Math.max(nums[0],nums[1],nums[2]);
    
    // rob 1st, not 2nd, not last
    var three_steps = nums[0]; // max at i - 3
    var two_steps = Math.max(nums[0],nums[1]); // max at i - 2
    var one_step = Math.max(nums[0]+nums[2],nums[1]); // max at i - 1
    var maxIncome = one_step;
    
    for (i = 3; i < arrayLength - 1; i++) {
        maxIncome = Math.max(maxIncome, Math.max(three_steps,two_steps) + nums[i]);
        three_steps = two_steps;
        two_steps = one_step;
        one_step = maxIncome;
    }
    
    // not rob 1st, rob 2nd, rob last
    three_steps = 0;
    two_steps = nums[1];
    one_step = Math.max(nums[2],nums[1]);
    var maxIncome2 = one_step;
    
    for (i = 3; i < arrayLength; i++) {
        maxIncome2 = Math.max(maxIncome2, Math.max(three_steps,two_steps) + nums[i]);
        three_steps = two_steps;
        two_steps = one_step;
        one_step = maxIncome2;
    }
    
    return Math.max(maxIncome,maxIncome2);
};

var r = 0
var arr = new Array(1,2,3,4,5,1,2,3,4,5)
r = rob(arr)
console.log(r);
