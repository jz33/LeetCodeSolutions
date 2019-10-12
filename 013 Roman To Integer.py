SymbolToInteger = {
    'I' : 1,
    'V' : 5,
    'X' : 10,
    'L' : 50,
    'C' : 100,
    'D' : 500,
    'M' : 1000,
}

class Solution:
    def romanToInt(self, roman: str) -> int:
        '''
        Use a more generalized method other than many if else conditions.
        Real onsite interview question with Amazon 2019-10-11
        '''
        res = 0
        i = 0
        while i < len(roman):
            c = roman[i]
            c_int = SymbolToInteger[c]
            inc = 0 # increase for i
            
            if i + 1 < len(roman):
                d = roman[i+1]
                d_int = SymbolToInteger[d]
                if d_int > c_int:
                    # IV, IX, XL, XC, CD, DM
                    res += d_int - c_int
                    inc = 2
            
            if inc == 0:
                res += c_int
                inc = 1
            
            i += inc
            
        return res
