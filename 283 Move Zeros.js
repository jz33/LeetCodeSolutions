/*
Move Zeros
https://leetcode.com/problems/move-zeroes/
*/
var moveZeroes = function(nums) {
    var i,j;
    for(i = 0,j = 0;i<nums.length;i++){
        if(nums[i] !== 0){
            nums[j++] = nums[i];
        }
    }
    for(;j<nums.length;j++){
        nums[j] = 0;
    }
};
