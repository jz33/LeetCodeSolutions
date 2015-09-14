/*
Basic Calculator II
https://leetcode.com/problems/basic-calculator-ii/

This solution works both on Basic Calculator and Basic Calculator II
*/
public class Solution {
    private int pos = 0;
    
    public int eval(String s){
        int res = 0;
        long prev = 0; // initial preVal is 0
        char sign = '+'; // initial sign is +
        while (pos < s.length()) {
            char c = s.charAt(pos);
            if(c == ' '){
                pos++;
                continue;
            }
            else if (c == ')'){
                pos++;
                return (int)(res + prev);
            }
            
            long curr = 0;
            if(c == '('){
                pos++;
                curr = eval(s);
            }
            else{
                while (pos < s.length() && Character.isDigit(s.charAt(pos))) {
                    curr = curr * 10 + Character.getNumericValue(s.charAt(pos));
                    pos++;
                } 
            }
            
            switch(sign){
                case '+':
                    res += prev;  // update res
                    prev = curr;
                    break;
                case '-':
                    res += prev;  // update res
                    prev = -curr;
                    break;
                case '*':
                    prev = prev * curr;
                    break;
                case '/':
                    prev = prev / curr;
                    break;
            }
            if (pos < s.length()) { // getting new sign
                if(s.charAt(pos) == ')'){
                    pos++;
                    return (int)(res + prev);
                }
                else{
                    sign = s.charAt(pos);
                    pos++;
                }
            }
        }
        return (int)(res + prev);
    }
    
    public int calculate(String s){
        if (s == null) return 0;
        s = s.trim();
        if(s.length() == 0) return 0;
        
        pos = 0;
        return eval(s);
    }
}
