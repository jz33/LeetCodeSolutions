"use strict";
/*
Longest Increasing Subsequence
https://leetcode.com/problems/longest-increasing-subsequence/
http://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
*/
/**
 * Find ceiling index of tag in arr
 * @param {number[]} arr
 * @param {number} tag
 * @return {number} range[-1,arr.length]
 */
var ceiling = function(arr,tag){
    var mid, v;
    for(var lt = 0, rt = arr.length - 1; lt <= rt;){
        mid = (lt + rt >> 1);
        v = arr[mid];
        if(v === tag) return -1; // found
        else if(v < tag) lt = mid + 1;
        else rt = mid - 1;
    }
    return lt;
}
/**
 * @param {number[]} arr
 * @return {number}
 */
var lengthOfLIS = function(arr){
    var i,j;
    var length = arr.length;
    var seq = [];

    for(i of arr){
        if(seq.length === 0 || seq[seq.length - 1] < i){                
            seq.push(i);
        }else{
            j = ceiling(seq, i);
            if(j >= 0) seq[j] = i;
        }
    }
    console.log(seq);
    return seq.length;
};
var arr = [10, 9, 2, 5, 3, 7, 101, 18]; // [2, 3, 7, 18]
console.log(lengthOfLIS(arr));
