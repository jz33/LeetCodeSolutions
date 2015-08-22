/**
 * @param {number[][]} grid
 * @return {number}
 */
var minPathSum = function(grid) {
    var i = 0, j = 0;
    var left = 0, up = 0;
    
    var n = grid.length;
    if(n === 0) return 0;
    var m = grid[0].length;
    if(m === 0) return 0;
    
    if(m === 1)
    {
        var r = grid[0][0];
        for(i = 1;i<n;i++)
            r += grid[i][0];
        return r;
    }
    
    var buf = Array.apply(null, Array(m-1)).map(Number.prototype.valueOf,0);
    left = grid[0][0];
    for(j = 0;j<m-1;j++){
        buf[j] = left + grid[0][j+1];
        left = buf[j];
    }
    
    var prev_left = grid[0][0];
    for(i = 1;i<n;i++){
        prev_left += grid[i][0];
        left = prev_left;
        for(j = 0;j<m-1;j++){
            up = buf[j];
            buf[j] = Math.min(left,up) + grid[i][j+1];
            left = buf[j];
        }
    }
    return buf[buf.length-1];
};
