"use strict";

var cache = [1];
var p2 = 0;
var p3 = 0;
var p5 = 0;

var nthUglyNumber = function(n) {
    var m,r2,r3,r5;
    var i = cache.length;
    for(;i < n ; i++)
    { 
        r2 = cache[p2] * 2;
        r3 = cache[p3] * 3;
        r5 = cache[p5] * 5;
        m = Math.min(r2,r3,r5);
        if(m === r2) p2++; 
        if(m === r3) p3++;
        if(m === r5) p5++;
        cache[i] = m;
    }
    return cache[n-1]; 
};
