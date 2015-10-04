/*
Text Justification
https://leetcode.com/problems/text-justification/
*/
"use strict";

var packWord = function(tag,pos,word){
    for(var i = 0;i<word.length;i++){
        tag[pos++] = word[i];
    }
    return pos;
}

var packSpace = function(tag,pos,space_length){
    for(var i = 0;i<space_length;i++){
        tag[pos++] = ' ';
    }
    return pos;
}

/**
 * @param {string[]} words
 * @param {number} width
 * @return {string[]}
 */
var fullJustify = function(words, width){
    var i,j,k;
    var pos,cul;
    var sl, sc; // space length, space count
    var ssl, ssc; // small space length, small space count 
    var lsc; //large space count
    var empty = [];
    var res = [];

    for(i = 0, j = 0, cul = 0;i < words.length;i++){
        if(words[i].length + cul + i - j - 1 >= width){
            console.dir("inner " + j+ " " +i + " " + cul);

            if(j + 1 === i){
                sl = width - cul;
                pos = packWord(empty,0,words[j]);
                packSpace(empty,pos,sl);
            } else {
                sl = width - cul;
                sc = i - j - 1;

                /*
                ssl * ssc + (ssl + 1) * (sc - ssc) = sl
                ssc = (ssl + 1) * sc - sl
                */
                ssl = parseInt(sl / sc);
                ssc = (ssl + 1) * sc - sl;
                lsc = sc - ssc;
                console.dir("ssl " + ssl + " " + ssc + " " + lsc);

                pos = 0;
                for(k = 0;k<lsc;k++){
                    pos = packWord(empty,pos,words[j++]);
                    pos = packSpace(empty,pos,ssl + 1);
                }
                for(k = 0;k<ssc;k++){
                    pos = packWord(empty,pos,words[j++]);
                    pos = packSpace(empty,pos,ssl);
                }
                packWord(empty,pos,words[j]);
            }
            cul = words[i].length;
            j = i;
            res.push(empty.join(''));
        } else {
            cul += words[i].length;
        }
    }

    // last
    for(pos = 0;pos < width && j < i - 1;){
        pos = packWord(empty,pos,words[j++]);
        pos = packSpace(empty,pos,1);
    }
    pos = packWord(empty,pos,words[j]);

    //console.log("pos: " + pos);
    packSpace(empty,pos,width - pos);
    res.push(empty.join(''));

    return res;
};


var words = ["This", "is", "an", "example", "of", "text", "justification."];
//var words = ["What","must","be","shall","be."];
//var words = [""];
//var words = ["a"];
var width = 16;
var res = fullJustify(words,width);
console.log(res);
