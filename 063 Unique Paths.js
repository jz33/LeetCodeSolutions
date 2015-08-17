/*
Unique Paths II
https://leetcode.com/problems/unique-paths-ii/
*/
/**
 * @param {number[][]} mat
 * @return {number}
 */
var uniquePathsWithObstacles = function(mat) {
    var i = 0;
    var j = 0;
    
    var n = mat.length;
    if(n === 0) return 0;
    
    var m = mat[0].length;
    if(m === 0) return 0;
    if(m === 1)
    {
        for(i = 0;i<n;i++)
            if(mat[i][0] === 1)
                return 0;
        return 1;
    }
    
    if(mat[0][0] === 1) return 0;
    
    var buf = Array.apply(null, Array(m - 1)).map(Number.prototype.valueOf,1);
    for(j = 0;j<m;j++)
        if(mat[0][j] === 1)
            break;
    for(;j<m;j++)
        buf[j-1] = 0;
    
    var lefts = Array.apply(null, Array(n - 1)).map(Number.prototype.valueOf,1);
    for(i = 0;i<n;i++)
        if(mat[i][0] === 1)
            break;
    for(;i<n;i++)
        lefts[i-1] = 0;
        
    for(i = 1;i<n;i++){
        var left = lefts[i-1];
        for(j = 0;j<m-1;j++){
            if(mat[i][j+1] !== 1)
                buf[j] = left + buf[j];
            else 
                buf[j] = 0;
            left = buf[j];
        }
    }
    return buf[m-2];
};
