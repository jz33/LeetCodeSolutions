/*
Add Digits
https://leetcode.com/problems/add-digits/
https://en.wikipedia.org/wiki/Digital_root
*/
var addDigits = function(num) {
    return 1 + (num - 1) % 9;
};
