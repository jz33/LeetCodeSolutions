/*
ZigZag Conversion
https://leetcode.com/problems/zigzag-conversion/
*/
/*
PAYPALISHIRING, 3 => PAHNAPLSIIGYIR
*/
var convert = function(s, nRows) {   
    if(nRows <= 1) return s;  
    if(s.length === 0) return "";
    
    var res = "";
    for(var i =0;i < nRows;i++){  
        for(var j = 0, index = i; index < s.length;j++, index = (2 * nRows - 2) * j +i){  
             res +=  s[index];  //red element
             if(i === 0 || i === nRows - 1)   //green element
                continue;  
 
             if(index + (nRows- i - 1) * 2 < s.length)  
                res += s[index + (nRows- i - 1) * 2];  
        }  
    }  
    return res;  
}

var r = convert("PAYPALISHIRING",3);
console.log(r)
