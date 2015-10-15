'''
Excel Sheet Column Title
https://leetcode.com/problems/excel-sheet-column-title/
Same like Binary to Decimal
'''
A = ord('A') - 1
Bits = 26
        
class Solution(object):
    def titleToNumber(self, s):
        j = 0
        r = 0
        for i in xrange(len(s)-1, -1 ,-1):
            r += Bits**j * (ord(s[i]) - A)
            j += 1
        return r
