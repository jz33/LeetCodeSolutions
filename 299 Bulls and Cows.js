/**
 * @param {string} secret
 * @param {string} guess
 * @return {string}
 */
var getHint = function(secret, guess) {
    var size = secret.length;
    var i,c,s;
    var ref = new Map(); // char : int
    var A = 0;
    var B = 0;
    
    for(i=0;i<size;i++){
        c = secret[i];
        if(c === guess[i]){
            A++;
        } else {
            s = ref.get(c);
            if(s === undefined){
                s = 0;
            }
            ref.set(c, s + 1);
        }
    }

    for(i=0;i<size;i++){
        c = guess[i];
        if(c !== secret[i]){
            s = ref.get(c);
            if(s !== undefined && s > 0){
                B++;
                ref.set(c, s - 1);
            }
        }
    }
    return A + 'A' + B + 'B';
};
