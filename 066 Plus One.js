/*
Plus One
https://leetcode.com/problems/plus-one/
*/
/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    var i = 0;
    for(i = digits.length - 1 ; i > -1;i--){
        if(digits[i] < 9){
            digits[i]++;
            return digits;
        } else {
            digits[i] = 0;
        }
    }
    digits.push(0);
    digits[0] = 1;
    return digits;
};
