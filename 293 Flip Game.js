"use strict";
/*
Flip Game
https://leetcode.com/problems/flip-game/

"++++" =>
[
  "--++",
  "+--+",
  "++--"
]
*/
var generatePossibleNextMoves = function(input){
    var res = [];
    var length = input.length;
    if(length < 2) return res;
    var list = input.split('');
    var prev = list[0];
    var newList,e;
    for(var i = 1; i < length; i++){
        e = list[i];
        if(e === '+' && prev === '+'){
            newList = [].concat(list);
            newList[i] = newList[i-1] = '-';
            res.push(newList.join(''));
        }
        prev = e;
    }
    return res;
};

var input = "--";
var res = generatePossibleNextMoves(input);
console.dir(res);
