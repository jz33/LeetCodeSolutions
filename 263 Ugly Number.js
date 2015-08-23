/**
 * @param {number} num
 * @return {boolean}
 */
 "use strict";
var isUgly = function(num) {
    for (var p of [2, 3, 5])
        while (num > 0 && num % p === 0)
            num /= p;
    return num == 1;
};
