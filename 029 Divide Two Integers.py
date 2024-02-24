'''
29. Divide Two Integers
https://leetcode.com/problems/divide-two-integers/

Given two integers dividend and divisor,
divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero,
which means losing its fractional part.
For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1].
For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.

Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.

Constraints:
    -231 <= dividend, divisor <= 231 - 1
    divisor != 0
'''
class Solution:
    '''
    Real TikTok interview question 20240125
    Approach 3: Adding Powers of Two
    '''
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants.
        MAX_INT = 2147483647        # 2**31 - 1
        MIN_INT = -2147483648       # -2**31

        # Special case: overflow.
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        if dividend == 0:
            return 0
        
        isPositive = dividend > 0 and divisor > 0 or dividend < 0 and divisor < 0 
        up = -dividend if dividend < 0 else dividend
        lo = -divisor if divisor < 0 else divisor
        
        quotient = 0

        # Enlarge power exponentially until up < lo
        power = 1
        while up >= lo:
            up -= lo
            quotient += power
            power <<= 1
            lo <<= 1

        # Now lo is bigger than up. Shrink exponentially
        power >>= 1
        lo >>= 1
        while up > 0 and power > 0:
            if up >= lo:
                up -= lo
                quotient += power
            power >>= 1
            lo >>= 1

        return quotient if isPositive else -quotient
    
sol = Solution()
tests = [
    (44, 3),
    (45, 3),
    (5, 5),
    (5, 1),
    (100, 2),
]
for d1, d2 in tests:
    print('{0} / {1} = {2}'.format(d1, d2, sol.divide(d1, d2)))

