"use strict";
/*
Valid Sudoku
https://oj.leetcode.com/problems/valid-sudoku/
*/
/**
 * @param {character[][]} mat
 * @return {boolean}
 */
var isValidSudoku = function(mat) {
    var full = 0x3FF; // 1111111111, last one is trivial
    var map,i,j,x,y,n;
    
    for(i = 0;i < 9;i++){
        map = full;
        for(j = 0;j < 9;j++){
            if(mat[i][j] !== "."){
                n = parseInt(mat[i][j],10);
                map = (map ^ (1 << n));
                if((map & (1 << n)) !== 0) {
                    return false;
                }
            }
        }
    }
    
    for(i = 0;i < 9;i++){
        map = full;
        for(j = 0;j < 9;j++){
            if(mat[j][i] !== "."){
                n = parseInt(mat[j][i],10);
                map = (map ^ (1 << n));
                if((map & (1 << n)) !== 0) {
                    return false;
                }
            }
        }
    }
    
    for(i = 0;i < 3;i++){        
        for(j = 0;j < 3;j++){
            map = full;
            for(x = i * 3; x < (i + 1) * 3 ; x++){
                for(y = j * 3; y < (j + 1) * 3; y++){
                    if(mat[x][y] !== "."){
                        n = parseInt(mat[x][y],10);
                        map = (map ^ (1 << n));
                        if((map & (1 << n)) !== 0) {
                            return false;
                        }
                    }
                }
            }
        }
    }
    return true;
};
