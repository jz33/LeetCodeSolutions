/*
152 Maximum Product Subarray
https://oj.leetcode.com/problems/maximum-product-subarray/
*/
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(arr) {
    if(arr.length === 0) return 0;
    
    var vMax = arr[0], vMin = arr[0], prev_vMax = 0,r = arr[0];
    
    arr.forEach(function(v,i,a){
        if(i > 0){
            prev_vMax = vMax;
            vMax = Math.max(v, v * vMax, v * vMin);
            vMin = Math.min(v, v * prev_vMax, v * vMin);
            r = Math.max(r,vMax);
        }
    });
    return r;
};
