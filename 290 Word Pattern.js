"use strict";
/*
Word Pattern
https://leetcode.com/problems/word-pattern/
*/
var wordPattern = function(pats, str){
    var i,p,r;
    var strs = str.split(' ');
    if(pats.length !== strs.length) return false;
    var map = new Map();
    var rev = new Map();
    for(i = 0; i< pats.length;i++){
        p = map.get(pats[i]);
        r = rev.get(strs[i]);
        if(p === undefined && r === undefined){
            map.set(pats[i],strs[i]);
            rev.set(strs[i],pats[i]);
        } else if (p !== undefined && r !== undefined){
            if(p !== strs[i] || r !== pats[i]) return false;
        } else {
            return false;
        }
    }   
    return true;
}

var pats = "abba";
var str = "dog cat cat fish";
console.log(wordPattern(pats, str));
