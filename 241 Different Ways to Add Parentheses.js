"use strict";
/*
Different Ways to Add Parentheses
https://leetcode.com/problems/different-ways-to-add-parentheses/
*/
/**
 * @param {string} input
 * @return {number[]}
 */
var diffWaysToCompute = function(input){
    var lt, rt;
    var arr = [];
    if(input === null || input === undefined) return arr;
    input.split('').forEach(function(op,i){
        if(op === '+' || op === '-' || op === '*'){
            lt = diffWaysToCompute(input.slice(0,i));
            rt = diffWaysToCompute(input.slice(i+1));
            
            lt.forEach(function(lv){
                rt.forEach(function(rv){
                    if(op === '+'){
                        arr.push(lv+rv);
                    } else if (op === '-'){
                        arr.push(lv-rv);
                    } else if (op === '*'){
                        arr.push(lv*rv);
                    }
                });
            });
        }
    });
    if(arr.length === 0) arr.push(parseInt(input));        
    return arr;
}

var input = "2-3-32";
var r = diffWaysToCompute(input);
console.dir(r);
