"use strict";
/*
3Sum
https://oj.leetcode.com/problems/15 3Sum/
*/
var threeSum = function(arr) {
    var pool = [];

    /*
    NOT:
    arr.sort();
    */
    arr.sort(function(x,y){
        return x - y;
    });
    
    var k = 0;
    while(k < arr.length - 2){
        var lt = arr[k];
        var i = k + 1;
        var j = arr.length - 1;
        while(i < j){
            var md = arr[i];
            var rt = arr[j];
            if(lt + md + rt === 0){
                pool.push([lt,md,rt]);
                
                i++;
                while(i<j && arr[i] === md) i++;
                j--;
                while(i<j && arr[j] === rt) j--;
            }
            else if(lt + md + rt < 0){
                i++;
                while(i<j && arr[i] === md) i++;
            }
            else{
                j--;
                while(i<j && arr[j] === rt) j--;
            }
        }
        k++;
        while(k < arr.length - 2 && arr[k] === lt) k++;
    }
    return pool;
};

var arr = [-1,-2,-3,4,5];
console.dir(JSON.stringify(threeSum(arr)));
