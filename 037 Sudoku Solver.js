"use strict";
/*
Sudoku Solver
https://leetcode.com/problems/sudoku-solver/

An iterative way
*/
var empty = 0x3FF; // 1111111111, last one is trivial
var ROW = 9;
var CELL = 3;

function Point(x,y){
    this.x = x;
    this.y = y;

    // possible numbers to put on current position
    // ps[0] records which one is chosen.
    this.ps = [];

    Object.defineProperty(this, "str",{
        get : function(){
            return this.x + ' ' + this.y + ' ' + JSON.stringify(this.ps);
        }
    });
}

var getValid = function(board,x,y){
    var map = [empty,empty,empty];
    var i,il,j,jl,n;
    var ps = [0];
    for(i = 0; i < ROW;i++){
        if(board[i][y] !== '.'){
            n = parseInt(board[i][y],10);
            map[0] ^= (1 << n);
        }
    }
    for(j = 0; j < ROW;j++){
        if(board[x][j] !== '.'){
            n = parseInt(board[x][j],10);
            map[1] ^= (1 << n);
        }
    }

    il = parseInt(x / CELL, 10) * CELL;
    jl = parseInt(y / CELL, 10) * CELL;

    for(i=il;i<il+CELL;i++){
        for(j=jl;j<jl+CELL;j++){
            if(board[i][j] !== '.'){
                n = parseInt(board[i][j],10);
                map[2] ^= (1 << n);
            }
        }
    }

    n = empty;
    map.forEach(function(v){
        n &= v;
    });

    for(i = 1;i <= ROW;i++){
        if((n & (1 << i)) !== 0){
            ps.push(i);
        } 
    }
    return ps;
};

var getEmptyPoints = function(board){
    var p = null;
    var valids = [];
    for(var i = 0;i < ROW;i++){
        for(var j = 0;j < ROW;j++){
            if(board[i][j] === '.'){
                valids.push(new Point(i,j));
            }
        }
    }
    return valids;
};

var solveSudoku = function(board){
    var arr = getEmptyPoints(board);
    var i,j,p;

    i = 0;
    while(i < arr.length){
        if(i < 0 || i === arr.length) return;

        p = arr[i];
        if(p.ps.length === 0 || p.ps[0] === 0){
            p.ps = getValid(board, p.x,p.y);
        }
        //console.log(p.str);
        p.ps[0]++;
        if(p.ps[0] === p.ps.length){
            // reset
            p.ps[0] = 0;
            board[p.x][p.y] = '.';
            i--;
        }
        else{
            board[p.x][p.y] = p.ps[p.ps[0]].toString();
            i++;
        }
    }
};

var board = [
['5','3','.','.','7','.','.','.','.'],
['6','.','.','1','9','5','.','.','.'],
['.','9','8','.','.','.','.','6','.'],
['8','.','.','.','6','.','.','.','3'],
['4','.','.','8','.','3','.','.','1'],
['7','.','.','.','2','.','.','.','6'],
['.','6','.','.','.','.','2','8','.'],
['.','.','.','4','1','9','.','.','5'],
['.','.','.','.','8','.','.','7','9'],
];

var r = solveSudoku(board);
console.log(board);
