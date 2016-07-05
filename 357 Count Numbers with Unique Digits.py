'''
357 Count Numbers with Unique Digits
https://leetcode.com/problems/count-numbers-with-unique-digits/
'''
def multi(x,y):
    p = 1
    for i in xrange(x,y,-1):
        p *= i
    return p
    
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        1 : 10
        2 : 10*9 + 1
        3 : 10*9*8 + 9*2 + 1
        4 : 10*9*8*7 + 9*2 + 9*8*3 + 1
        5 : 10*9*8*7*6 + 9*2 + 9*8*3 + 9*8*7*4 + 1
        ...
        """
        if n == 0: return 1
        if n == 1: return 10
        
        width = 10 if n > 10 else n
        pool = multi(10,10-width)
        for i in xrange(2,width):
            pool += multi(9,10-i) * i
        return pool + 1
