"use strict";
/*
Shortest Word Distance III

Given a string list and 2 words,
return the shortest distance between these two words in the list.

e.g,
list = ["practice", "makes", "perfect", "coding", "makes"].

x = "makes", y = "makes", => 3.
x = "makes",  y = "coding", => 1.

Note:
x and y may be the same, 
and they represent two individual words in the list.
*/
var shortestWordDistance = function(list,x,y){
    var dist = Number.MAX_SAFE_INTEGER;
    var px = -1;
    var py = -1;
    list.forEach(function(v,i){
        if(v === x){
            if(x !== y) px = i;
            else{
                py = px;
                px = i;
            }
        }
        if(v === y){
            if(x !== y) py = i; 
        }
        if(px != -1 && py != -1){
            dist = Math.min(dist,Math.abs(px-py));
        }
    });
    return dist;
}

var list = ["practice", "makes", "perfect", "coding", "makes"];
var x = "makes";
var y = "makes";
console.log(shortestWordDistance(list,x,y));

x = "practice";
y = "coding";
console.log(shortestWordDistance(list,x,y));
