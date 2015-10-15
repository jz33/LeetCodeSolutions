'''
Excel Sheet Column Title
https://leetcode.com/problems/excel-sheet-column-title/
Same like Decimal to Binary
'''
A = ord('A') - 1
Bits = 26

class Solution(object):
    def convertToTitle(self, d):
        ls = []
        while d > 0:
            r = d % Bits
            if r == 0 : r = Bits
            d = ( d - 1 ) /Bits
            ls.append(chr(A + r))
        ls.reverse()
        return ''.join(ls)
