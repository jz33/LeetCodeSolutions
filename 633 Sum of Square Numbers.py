'''
633. Sum of Square Numbers
https://leetcode.com/problems/sum-of-square-numbers/

Given a non-negative integer c,
decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:

Input: c = 5
Output: true
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:

Input: c = 3
Output: false

Constraints:
    0 <= c <= 231 - 1
'''
from math import sqrt

def isSquare(bs: int)-> bool:
    root = int(sqrt(bs))
    return root * root == bs

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while a * a <= c:
            bs = c - a * a
            if isSquare(bs):
                return True
            a += 1
        return False