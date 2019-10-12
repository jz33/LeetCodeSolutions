IntergerToRoman = {
    1   : 'I',
    5   : 'V',
    10  : 'X',
    50  : 'L',
    100 : 'C',
    500 : 'D',
    1000: 'M',
}

class Solution:
    def intToRoman(self, num: int) -> str:
        '''
        Use a more generalized method other than many if else conditions.
        Real onsite interview question with Amazon 2019-10-11
        '''
        res = []
        for p in range(3,-1,-1): # 3, 2, 1, 0
            base = 10 ** p
            if num >= 9 * base:
                res += [IntergerToRoman[base], IntergerToRoman[base*10]]
                num -= 9 * base             
            elif num >= 5 * base:
                res += [IntergerToRoman[base*5]]
                num -= 5 * base
            elif num >= 4 * base:
                res += [IntergerToRoman[base], IntergerToRoman[base*5]]
                num -= 4 * base
            
            t = num // base
            if t > 0:             
                num -= t * base
                res += [IntergerToRoman[base]] * t
        
        return ''.join(res)
