"use strict";
/*
Pascal's Triangle
https://oj.leetcode.com/problems/pascals-triangle/
*/
var generate = function(numRows) {
    var mat = [];
    var row = [];
    for(var i = 0;i < numRows;i++){
        // push front
        row.splice(0,0,1);
        for(var j = 1;j < row.length - 1;j++){
           row[j] =  row[j] + row[j+1]; 
        }
        // deepcopy
        mat.push(([]).concat(row));
    }
    return mat;
};

var r = generate(5);
console.dir(JSON.stringify(r));
