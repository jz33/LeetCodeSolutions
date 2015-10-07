"use strict";
/*
Shortest Word Distance

Given a string list and 2 words,
return the shortest distance between these two words in the list.

e.g,
list = ["practice", "makes", "perfect", "coding", "makes"].

x = "coding", y = "practice", => 3.
x = "makes",  y = "coding", => 1.

Note:
You may assume that x does not equal to y, 
and x and y are both in the list.
*/
var shortestWordDistance = function(list,x,y){
    var dist = Number.MAX_SAFE_INTEGER;
    var px = -1;
    var py = -1;
    list.forEach(function(v,i){
        if(v === x) px = i;
        if(v === y) py = i;
        if(px != -1 && py != -1){
            dist = Math.min(dist,Math.abs(px-py));
        }
    });
    return dist;
}

var list = ["practice", "makes", "perfect", "coding", "makes"];
var x = "coding";
var y = "practice";
console.log(shortestWordDistance(list,x,y));

x = "makes";
y = "coding";
console.log(shortestWordDistance(list,x,y));
