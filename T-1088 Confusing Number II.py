'''
1088. Confusing Number II
https://leetcode.com/problems/confusing-number-ii/

We can rotate digits by 180 degrees to form new digits. When 0, 1, 6, 8, 9 are rotated 180 degrees,
they become 0, 1, 9, 8, 6 respectively. When 2, 3, 4, 5 and 7 are rotated 180 degrees, they become invalid.

A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.
(Note that the rotated number can be greater than the original number.)

Given a positive integer N, return the number of confusing numbers between 1 and N inclusive.

Example 1:

Input: 20
Output: 6
Explanation: 
The confusing numbers are [6,9,10,16,18,19].
6 converts to 9.
9 converts to 6.
10 converts to 01 which is just 1.
16 converts to 91.
18 converts to 81.
19 converts to 61.

Example 2:

Input: 100
Output: 19
Explanation: 
The confusing numbers are [6,9,10,16,18,19,60,61,66,68,80,81,86,89,90
'''
import itertools
from typing import Tuple

class Solution:
    def strobogrammaticCountWithWidth(self, width: int) -> int:
        if width == 0:
            return 0
        if width == 1:
            return 3 # [0, 1, 8]

        isEven = (width & 1) == 0
        if isEven:
            # The first digit can only be [1,6,8,9], others can only be [0,1,6,8,9]
            return 4 * (5 ** (width // 2 - 1))
        else:
            # The first digit can only be [1,6,8,9], middle can only be [1,8,0], others can only be [0,1,6,8,9]
            return 4 * (5 ** (width // 2 - 1)) * 3  

    def confusingCountWithWidth(self, width: int) -> int:
        if width == 0:
            return 0
        if width == 1:
            return 2 # [6, 9]

        # For all numbers composed by [0,1,6,8,9], if they are not strobogrammic number, they are confusing number
        return 4 * 5 ** (width-1) - self.strobogrammaticCountWithWidth(width)

    def isConfusingNumber(self, num: Tuple[int]) -> bool:
        for i in range(len(num) // 2 + 1):
            e = num[i]
            if e == 0 or e == 1 or e == 8:
                if num[-(i+1)] != e:
                    return True
            elif e == 6:
                if num[-(i+1)] != 9:
                    return True
            elif e == 9:
                if num[-(i+1)] != 6:
                    return True
                
        return False

    def confusingNumberII(self, N: int) -> int:
        # width = 0, 1 cases
        if N < 6:
            return 0
        if N < 9:
            return 1
        if N < 10:
            return 2

        strN = str(N)
        width = len(strN)

        belowCount = sum(self.confusingCountWithWidth(i) for i in range(width))

        countOnWidth = 0
        for tup in itertools.product([0,1,6,8,9], repeat=width):
            if tup[0] != 0:
                if self.isConfusingNumber(tup):
                    if ''.join(str(j) for j in tup) <= strN:
                        countOnWidth += 1
                    else:
                        # As the product is in order, do early break
                        break
        return belowCount + countOnWidth

    
pairs = {0: 0, 1: 1, 6: 9, 8: 8, 9: 6}
    
class Solution:
    '''
    TLE
    '''
    def confusingNumberII(self, N: int) -> int:      
        count = 0
        
        def dfs(num, reversedNum, decimal):
            nonlocal count
            count += num != reversedNum
            for digit, reversedDigit in pairs.items():
                nextNum = num * 10 + digit
                if nextNum <= N:
                    dfs(nextNum, reversedDigit * decimal + reversedNum, decimal * 10)
                    
        if N >= 1: dfs(1,1,10)
        if N >= 6: dfs(6,9,10)
        if N >= 8: dfs(8,8,10)
        if N >= 9: dfs(9,6,10)
            
        return count
