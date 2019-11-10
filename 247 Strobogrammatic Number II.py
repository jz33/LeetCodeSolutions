'''
247. Strobogrammatic Number II

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Find all strobogrammatic numbers that are of length = n.
'''
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        isEven = (n & 1) == 0
        base = [''] if isEven else ['0','1','8']    
        start = 2 if isEven else 3
        res = base
        for _ in range(start,n+1,2):
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
