"use strict";
/*
Subsets
https://oj.leetcode.com/problems/subsets/
*/
"use strict";

var subsets = function(arr){
    arr.sort(function(x,y){
        return x - y;
    });

    var bits = arr.length;
    var size = 1 << bits;

    var pool = [];
    for(var i = 0;i<size;i++){
        var row = [];
        for(var j = 0;j < bits;j++){
            
            // Notice operator precedence
            if((1 << j & i) !== 0){
                row.push(arr[j]);
            }
        }
        pool.push(row);
    }
    return pool;
};

var arr = [3,2,1];
console.dir(subsets(arr));
