'''
479. Largest Palindrome Product
https://leetcode.com/problems/largest-palindrome-product/

Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, you should return the largest palindrome mod 1337.

Example:

Input: 2
Output: 987
Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

Note:

The range of n is [1,8].
'''
from math import sqrt

class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9

        upper = 10 ** n - 1 # inclusive
        lower = 10 ** (n - 1) - 1 # exclusive
        maxUpper = upper ** 2
        for v in range(upper, lower, -1):
            p = int(str(v) + str(v)[::-1])
            if p > maxUpper:
                continue
            for d in range(upper, max(int(sqrt(p)) - 1, lower), -1):
                if p % d == 0:
                    # print(p, d)
                    return p % 1337

        return 0
