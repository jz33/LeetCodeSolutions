/*
Integer to English Words
https://leetcode.com/problems/integer-to-english-words/
https://leetcode.com/discuss/55462/my-clean-java-solution-very-easy-to-understand
*/
public class Solution {
    String[] lessThan20 = {"","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"};
    String[] tens = {"","Ten","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"};
    String[] thousands = {"", "Thousand", "Million", "Billion"};

    public String numberToWords(int num) {
        if (num == 0) return "Zero";
        
        String words = "";
        for(int i = 0;num > 0;i++){
            int r = num % 1000;
            if (r != 0){
                words = rec(r) + thousands[i] + " " + words;
            }
            num /= 1000;
        }
        return words.trim();
    }
    
    public String rec(int r){
        if (r == 0)
            return "";
        else if (r < 20)
            return lessThan20[r] + " ";
        else if (r < 100)
            return tens[r/10] + " " + rec(r%10);
        else
            return lessThan20[r/100] + " Hundred " + rec(r%100);
    }
}
