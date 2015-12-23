/**
 * @param {string} word
 * @return {string[]}
 */
var generateAbbreviations = function(word) {
    var i,j,c;
    var size = word.length;
    var width = 1 << size;
    
    var res = [];
    var ls = [];
    for(i=0;i<width;i++){
        ls = [];
        c = 0;
        for(j=0;j<size;j++){
            if(1 << j & i){
                if(c) ls.push(c.toString());
                c = 0;
                ls.push(word[j]);
            } else {
                c++;
            }
        }
        if(c) ls.push(c);
        res.push(ls.join(''));
    }
    return res;
};
