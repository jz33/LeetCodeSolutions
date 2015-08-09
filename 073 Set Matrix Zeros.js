/**
 * @param {number[][]} mat
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
var setZeroes = function(mat)
{
    if(mat.length === 0) return;
    
    var firstColumnIsZero = false;
    var firstRowIsZero = false;
    
    // first column
    var i = 0;
    for(i=0;i<mat.length;i++)
        if(mat[i][0] === 0)
        {
            firstColumnIsZero = true;
            break;
        }
    
    // first row
    var j = 0;
    for(j=0;j<mat[0].length;j++)
        if(mat[0][j] === 0)
        {
            firstRowIsZero = true;
            break;
        }
    
    // mark
    for(i=1;i<mat.length;i++)
        for(j=1;j<mat[i].length;j++)
            if(mat[i][j] === 0)
            {
                mat[i][0] = 0;
                mat[0][j] = 0;
            }
    
    // makr by column
    for(i=1;i<mat.length;i++)
        if(mat[i][0] === 0)
            for(j = 1;j<mat[i].length;j++)
                mat[i][j] = 0;
    
    // mark by row
    for(j=1;j<mat[0].length;j++)
        if(mat[0][j] ===0)
            for(i=1;i<mat.length;i++)
                mat[i][j] = 0;
    
    // mark first column
    if(firstColumnIsZero)
        for(i=0;i<mat.length;i++)
            mat[i][0] = 0;
            
    // mark first row
    if(firstRowIsZero)
        for(j=0;j<mat[0].length;j++)
            mat[0][j] = 0;
};
