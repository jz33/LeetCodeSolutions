"use strict";
/*
Pascal's Triangle II
https://leetcode.com/problems/pascals-triangle-ii/
*/
var getRow = function(rowIndex) {
    var row = [];
    for(var i = 0;i <= rowIndex;i++){
        // push front
        row.splice(0,0,1);
        for(var j = 1;j < row.length - 1;j++){
           row[j] =  row[j] + row[j+1]; 
        }
    }
    return row;
};

var rowIndex = process.argv[2];
var row = getRow(rowIndex);
console.dir(JSON.stringify(row));
