"use strict";
/*
Remove Duplicate Letters
https://leetcode.com/problems/remove-duplicate-letters/
*/
/**
 * @param {string} s
 * @return {string}
 */
var removeDuplicateLetters = function(s){
    var i,ch,df;
    var A = 'a'.charCodeAt(0);
    var len = s.length;
    var ctr = new Array(26).fill(0);
    for(i = 0;i<len;i++){
        ctr[s.charCodeAt(i) - A]++;
    }

    var mp = 0; // position of minimun char
    var res = [];
    for(i = 0;i<len;i++){
        ch = s[i];
        df = s.charCodeAt(i) - A

        // previously added
        if(ctr[df] < 0) continue;

        if(ch < s[mp]) mp = i;
        ctr[df]--;

        if(ctr[df] === 0){
            ctr[s.charCodeAt(mp) - A] = -len;
            res.push(s[mp]);
            console.log(ctr);

            // move mp to valid position
            while(mp < len && ctr[s.charCodeAt(mp) - A] < 0) 
                mp++;

            // move i back to mp
            while(i >= mp){
                ctr[s.charCodeAt(i) - A]++;
                i--;
            }
            // i === mp at next round
            console.log(mp + ", "+i);
        }
    }
    return res.join('');
};

console.log(removeDuplicateLetters(process.argv[2]));
