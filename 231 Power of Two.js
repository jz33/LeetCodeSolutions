/*
Power of Two
https://leetcode.com/problems/power-of-two/
*/
var isPowerOfTwo = function(n) {
    return (n > 0) && !(n & (n - 1));
};
