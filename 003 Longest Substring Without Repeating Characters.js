/*
03 Longest Substring Without Repeating Characters
https://oj.leetcode.com/problems/longest-substring-without-repeating-characters/
*/
/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLongestSubstring = function(input){
    if(input.length < 2) return input.length;
    var buf = Array.apply(null, Array(256)).map(Number.prototype.valueOf,0);
    var lt = 0;
    var maxLen = 1;
    var i = 0;
    for(;i<input.length;i++){
        var c = input.charCodeAt(i);
        if(buf[c] === 0){
            buf[c] = 1;
        } else {
            maxLen = Math.max(maxLen,i-lt);
            while(lt < i && input.charCodeAt(lt) != c)
            { 
                buf[input.charCodeAt(lt)] = 0;
                lt++;
            }
            lt++;
        }
    }
    //process.stdout.write("i: "+i+ " lt: "+lt+"\n");
    maxLen = Math.max(maxLen,i-lt);
    return maxLen;
};

var cases = new Array(
    "aa",
    "eeeeeee",
    "abcd",
    "abcda",
    "abcdc",
    "abcdcefg",
    "tmmzuxt" //5
);
cases.forEach(function(e, i, arr){
    process.stdout.write(e + " : " +lengthOfLongestSubstring(e)+"\n");
});
