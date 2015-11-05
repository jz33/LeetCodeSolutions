"use strict";
/*
Fraction to Recurring Decimal
https://leetcode.com/problems/fraction-to-recurring-decimal/

Notice "parseInt" can be failed on small number, i.e,
1 / 214748364
Use Math.floor
*/
/**
 * @param {number} numerator
 * @param {number} denominator
 * @return {string}
 */
var fractionToDecimal = function(numerator, denominator) {
    var res = [];
    if (numerator > 0 && denominator < 0 || 
        numerator < 0 && denominator > 0) 
        res[0] = '-';
    var x = Math.abs(numerator);
    var y = Math.abs(denominator);
    res.push(Math.floor(x/y));
    var r = x % y; // remainder
    if(r !== 0){
        res.push('.');
        var map = new Map();
        while(map.has(r) === false){
            map.set(r,res.length);
            res.push(Math.floor(10 * r / y));
            r = 10 * r % y;
        }
        var start = map.get(r);
        // last digit will be '0' for non-recurring decimal
        if (res[start] === 0 && start == res.length - 1){
            res.splice(start,1);
        } else {
            res.splice(start,0,'(');
            res.push(')');
        }
    }
    return res.join('');
};

var numerator = parseInt(process.argv[2]);
var denominator = parseInt(process.argv[3]);
console.log(fractionToDecimal(numerator, denominator));
