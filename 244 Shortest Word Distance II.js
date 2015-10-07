"use strict";
/*
Shortest Word Distance II

Given a string list and 2 words,
return the shortest distance between these two words in the list.

e.g,
list = ["practice", "makes", "perfect", "coding", "makes"].

x = "coding", y = "practice", => 3.
x = "makes",  y = "coding", => 1.

Note:
You may assume that x does not equal to y, 
and x and y are both in the list.

If the list is huge and this function is called many times,
how to optimize?
*/

// A Closure
var shortestWordDistance = function(list){
    var map = new Map();
    var arr;
    list.forEach(function(v,i){
        arr = map.get(v);
        if(arr === undefined){
            map.set(v,[i]);
        } else {
            arr.push(i);
            map.set(v,arr);
        }
    });
    
    var compute = function(x,y){
        var arr_x = map.get(x);
        var arr_y = map.get(y);
        var dist = Number.MAX_SAFE_INTEGER;
        var i,j;
        for(i = 0,j = 0; i < arr_x.length && j < arr_y.length;){
            dist = Math.min(dist, Math.abs(arr_x[i] - arr_y[j]));
            if(arr_x[i] < arr_y[j]) i++;
            else j++;
        }
        return dist;
    }
    return compute;
}

var list = ["practice", "makes", "perfect", "coding", "makes"];
var func = shortestWordDistance(list);
var x = "coding";
var y = "practice";
console.log(func(x,y));

x = "makes";
y = "coding";
console.log(func(x,y));
