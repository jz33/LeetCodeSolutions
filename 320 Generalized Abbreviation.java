import java.util.*;
/*
320 Generalized Abbreviation
https://leetcode.com/problems/generalized-abbreviation/
*/
public class Solution {
    
    private ArrayList<String> ans = new ArrayList<String>();
    private String word = "";
    
    public void rec(StringBuffer sb, int pos){
        int len = sb.length();
        if(pos >= word.length()){
            ans.add(sb.toString());
        } else if (pos == word.length() - 1){
            // Optimization
            sb.append(word.charAt(pos));
            ans.add(sb.toString());
            sb.delete(len,sb.length());
            sb.append(1);
            ans.add(sb.toString());
            sb.delete(len,sb.length());
        } else {
            for(int i = 1;i < word.length() - pos;i++){
                sb.append(i);
                sb.append(word.charAt(pos+i));
                rec(sb,pos+i+1);
                sb.delete(len,sb.length());
            }
            
            // w, 1 => w3
            sb.append(word.length() - pos);
            ans.add(sb.toString());
            sb.delete(len,sb.length());
            
            // w, 1 => wo, 2
            sb.append(word.charAt(pos));
            rec(sb,pos+1);
            sb.delete(len,sb.length());
        }
    }
    
    public List<String> generateAbbreviations(String word) {
        this.ans.clear();
        this.word = word;
        StringBuffer sb = new StringBuffer();
        rec(sb,0);
        return this.ans;
    }
}
