/*
Next Permutation
https://leetcode.com/problems/next-permutation/
https://leetcode.com/discuss/24515/9-lines-of-c-code-with-comments
*/
/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var nextPermutation = function(nums) {
    var i,j,k,t;
    if(nums === null || nums === undefined || nums === '') return;
    
    // in reverse order, find the first number which is in increasing trend (we call it violated number here)
    for(i = nums.length - 2;i > -1;i--){
        if (nums[i] < nums[i+1]) break;
    }
    
    // reverse all the numbers after violated number
    for(j = i + 1, k = nums.length - 1; j < k;j++,k--){
        t = nums[j];
        nums[j] = nums[k];
        nums[k] = t;
    }
    //console.log(nums);
    
    // if violated number not found, because we have reversed the whole array, then we are done!
    if(i === -1) return;
    
    // else binary search find the first number larger than the violated number
    for(j = i+1;j < nums.length;j++){
        if(nums[j] > nums[i]) break;
    }
    // console.log(i,j);
    // swap them, done!
    t = nums[i];
    nums[i] = nums[j];
    nums[j] = t;
};
