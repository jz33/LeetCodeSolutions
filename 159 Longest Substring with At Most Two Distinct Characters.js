"use strict";
/*
Longest Substring with At Most Two Distinct Characters
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
*/
var lengthOfLongestSubstringTwoDistinct = function(input){
    var length = input.length;
    if(length < 3) return length;
    var res = '';
    var i,j,c,v;
    var map = new Map();
    for(i=0, j=0;i<length;i++){
        c = input.charAt(i);
        v = map.get(c);
        if(v === undefined){
            map.set(c,1);
        } else {
            map.set(c,v+1);
        }
        while(map.size > 2){
            c = input.charAt(j);
            v = map.get(c);
            if(v === 1){
                map.delete(c);
            } else {
                map.set(c,v-1);
            }
            j++;
        }
        if(i+1-j > res.length) res = input.slice(j,i+1);
    }
    console.log(res);
    return res.length;
}

var input = "abaerwfacsqefav";
console.log(lengthOfLongestSubstringTwoDistinct(input));
