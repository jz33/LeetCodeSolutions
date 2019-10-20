'''
166. Fraction to Recurring Decimal
https://leetcode.com/problems/fraction-to-recurring-decimal/

Given two integers representing the numerator and denominator of a fraction,
return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"

Input: numerator = 1, denominator = 6
Output: "0.1(6)"
'''
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:        
        # Result contains either digit or string
        res = []      
        
        # 1. Interger part
        if numerator > 0 and denominator < 0 or numerator < 0 and denominator > 0:
            res.append('-')

        # Trap: do not direcly put numerator // denominator
        # -3 // 4 is -1 not 0 !
        n = abs(numerator)
        d = abs(denominator)
        res.append(n // d)

        # 2. Decimal part     
        r = n % d # remainder
        if r > 0:
            res.append('.')
            decimals = []

            # @ rs records appeared remainders and their first appeared index.
            rs = {}
            while r != 0 and r not in rs:
                rs[r] = len(decimals)
                decimals.append(r * 10 // d)
                r = r * 10 % d
            
            # If decimal is terminating, r is 0.
            # Otherwise decimal is recurring.
            if r == 0:
                res += decimals
            else:
                # recur[cut:] is the recurring part
                cut = rs[r]
                res += decimals[:cut]
                res.append('(')
                res += decimals[cut:]
                res.append(')')
        
        return ''.join(str(e) for e in res)
