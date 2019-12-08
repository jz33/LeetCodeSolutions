'''
273. Integer to English Words
https://leetcode.com/problems/integer-to-english-words/

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 2^31 - 1.

Example 1:
Input: 123
Output: "One Hundred Twenty Three"

Example 2:
Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:
Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
'''
Under20 = ["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"];
Under100 = ["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"];
Thousands = ["", "Thousand", "Million", "Billion"];

class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        
        # Iterate reversely to deal with very large numbers
        words = []
        i = 0
        while num > 0:
            s = self.under1000(num % 1000)
            if s:
                if i == 0:
                    words.append(s)
                else:
                    words.append(s + ' ' + Thousands[i])
            i += 1
            num = num // 1000
        return ' '.join(words[::-1])
    
    def under1000(self, r: int) -> str:
        words = []
        if r >= 100:
            words += [Under20[r // 100], 'Hundred']
            r = r % 100
        if r >= 20:
            words.append(Under100[r // 10])
            r = r % 10
        if r > 0:
            words.append(Under20[r])
        return ' '.join(words)
