/*
282 Expression Add Operators
https://leetcode.com/problems/expression-add-operators/
"123", 6 -> ["1+2+3", "1*2*3"] 
"232", 8 -> ["2*3+2", "2+3*2"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
*/

var addOperators = function(expr, tag){
    var ans = [];
    if(expr === null || expr.length === 0) return ans;
    rec(expr, tag, ans, "", 0,0,0);
    return ans;
};

/*
pos : position of expr
prev: previous result
multi: previous number that is ready for multiplication at current step
*/
var rec = function(expr, tag, ans, path, pos, prev, multi){
    if (pos == expr.length){
        if(tag == prev){
            ans.push(path);
        }
    }
    else{
        for(var i = pos + 1; i <= expr.length; i++){
            var n = parseInt(expr.substring(pos, i), 10);
            var s = n.toString();
            
            // i.e., "01"
            if(s.length != i - pos) break;
            if(pos === 0){
                rec(expr, tag, ans, path + s, i, n, n);
            }
            else{
                rec(expr, tag, ans, path + "+" + s, i, prev + n,  n);
                rec(expr, tag, ans, path + "-" + s, i, prev - n, -n);
                rec(expr, tag, ans, path + "*" + s, i, prev - multi + multi * n, multi * n );
            }
        }
    }
}

var expr = "123";
var tag = 6;
var ans = addOperators(expr,tag);
console.dir(ans);
