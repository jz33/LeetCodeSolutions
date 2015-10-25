/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isOneEditDistance = function(s, t) {
    var ls = s.length;
    var lt = t.length;
    if(ls === 0) return lt === 1;
    if(lt === 0) return ls === 1;
    if(lt - ls > 1 || ls - lt > 1) return false;

    if(ls > lt){
       var m = s;
       s = t;
       t = m;
    }
    
    ls = s.length;
    lt = t.length;
    var i,j;
    if(lt - ls === 1){
        for(i = 0,j = 0;i < ls && j - i < 2;i++,j++){
            if(s[i] !== t[j]){
                i--;
            }
        }
        console.log(i +", "+j);
        return j - i < 2;
    }
    
    m = 0;
    for(i = 0;i< ls && m < 2;i++){
        if(s[i] !== t[i]) m++;
    }
    return m === 1;
};
