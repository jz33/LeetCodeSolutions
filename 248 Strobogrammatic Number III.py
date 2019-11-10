'''
248. Strobogrammatic Number III
https://leetcode.com/problems/strobogrammatic-number-iii/

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to count the total strobogrammatic numbers that exist in the range of low <= num <= high.

Example:

Input: low = "50", high = "100"
Output: 3 
Explanation: 69, 88, and 96 are three strobogrammatic numbers.
Note:
Because the range might be a large number, the low and high numbers are represented as string.
'''
class Solution:
    def strobogrammaticNumbersWithWidth(self, width: int) -> List[str]:
        isEven = (width & 1) == 0
        base = [''] if isEven else ['0','1','8']    
        start = 2 if isEven else 3
        res = base
        for _ in range(start,width+1,2):
            newBase = []
            newRes = []
            for s in base:
                for a, b in [('0','0'), ('1','1'), ('6','9'), ('8','8'), ('9','6')]:
                    newBase.append(a + s + b)
                for a, b in [('1','1'), ('6','9'), ('8','8'), ('9','6')]:
                    # Do not add '0' as number cannot start from 0
                    newRes.append(a + s + b)
            base = newBase
            res = newRes
        return res

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
    
    def strobogrammaticCountBelowBound(self, bound: str, include: bool) -> int:
        width = len(bound)
        countBelow = sum(self.strobogrammaticCountWithWidth(w) for w in range(width))
        countWidth = self.strobogrammaticNumbersWithWidth(width)
        
        if include:
            return countBelow + sum(1 for st in countWidth if len(st) == width and st <= bound)
        else:
            return countBelow + sum(1 for st in countWidth if len(st) == width and st < bound)

    def strobogrammaticInRange(self, low: str, high: str) -> int:
        highCount = self.strobogrammaticCountBelowBound(high, True)
        lowCount = self.strobogrammaticCountBelowBound(low, False)
        return highCount - lowCount if highCount > lowCount else 0
