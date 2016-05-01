'''
Integer to English Words
https://leetcode.com/problems/integer-to-english-words/
'''
lessThan20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"];
tens = ["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"];
thousands = ["", "Thousand", "Million", "Billion"];
    
class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return "Zero";
        words = [];
        i = 0
        while num > 0:
            r = self.under1000(num % 1000)
            if r != '':
                if i != 0:
                    words.append(r + " " + thousands[i])
                else:
                    words.append(r)
            num /= 1000
            i += 1
        return ' '.join(words[::-1]);
        
    def under1000(self,r):
        sb = []
        if r >= 100:
            sb.append(lessThan20[r/100])
            sb.append("Hundred");
            r = r % 100;
        if r >= 20:
            sb.append(tens[r/10]);
            r = r % 10;
        if r > 0:
            sb.append(lessThan20[r]);
        return ' '.join(sb)
    
