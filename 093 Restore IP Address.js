/*
93. Restore IP Addresses
https://leetcode.com/problems/restore-ip-addresses/

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
*/
/**
 * @param {string} s
 * @return {string[]}
 */
var restoreIpAddresses = function(s) {
    var a,b,c,d,i,j,k,ip;
    var res = [];
    var len = s.length;
    for(i = 1;i <= 3; ++i) {
        for (j = i+1;j <= i+3; ++j) {
            for (k = j+1; k <= j+3 && k < len; ++k) {
                a = parseInt(s.substring(0,i),10);  
                b = parseInt(s.substring(i,j),10);
                c = parseInt(s.substring(j,k),10);
                d = parseInt(s.substring(k),  10);
                if (a <= 255 && b <= 255 && c <= 255 && d <= 255) {
                    ip = a + "." + b + "." + c + "." + d;
                    if (ip.length === len + 3) {
                        res.push(ip);
                    }
                }
            }
        }
    }
    return res;
};
