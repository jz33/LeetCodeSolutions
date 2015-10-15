/*
Happy Number
https://leetcode.com/problems/happy-number/
*/
var digitSquareSum = function(x){
    var r = 0;
    var d = 0;
    while(x > 0){
        d = x % 10;
        r += d * d;
        x = parseInt(x / 10);
    }
    return r;
} 
 
var isHappy = function(n) {
    var slow = n;
    var fast = n;
    do{
        slow = digitSquareSum(slow);
        fast = digitSquareSum(fast);
        fast = digitSquareSum(fast);
    } while(slow != fast);
    return slow === 1;
};
