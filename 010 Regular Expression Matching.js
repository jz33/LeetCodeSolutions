"use strict";
/*
Regular Expression Matching
https://leetcode.com/problems/regular-expression-matching/
*/
/*
Notice "String.splice" out of bound will produce emtry string ""
*/
var isMatch = function(s, p){
    // "" -> ""
    if(p === "") 
        return s === "";
    
    // "" -> "" || ".*.*"
    if(s === "")
        return p.charAt(1) === '*' && isMatch(s, p.slice(2));
    
    // "a" -> "a" || "."
    if(p.charAt(1) !== '*')
        return (p.charAt(0) === '.' || p.charAt(0) === s.charAt(0)) 
            && isMatch(s.slice(1), p.slice(1));
    
    // p[1] == '*'
    // 0. skip '*'
    return isMatch(s, p.slice(2)) ||
                
    // 1. '*' matches more than 1 chars
    (p.charAt(0) === '.' || p.charAt(0) === s.charAt(0)) && isMatch(s.slice(1), p);
}

console.dir(isMatch("aa","aa"));
