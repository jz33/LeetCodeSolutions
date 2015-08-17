/*
Unique Paths
https://leetcode.com/problems/unique-paths/
*/
/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    if(m <= 1) return 1;
    if(n <= 1) return 1;
    
    var buf = Array.apply(null, Array(m-1)).map(Number.prototype.valueOf,1);
    for(var i = 1;i<n;i++){
        var left = 1;
        for(var j = 0;j<m-1;j++){
            buf[j] = left + buf[j];
            left = buf[j];
        }
    }
    return buf[buf.length-1];
};
