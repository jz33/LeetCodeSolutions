'''
777. Swap Adjacent in LR String
https://leetcode.com/problems/swap-adjacent-in-lr-string/

In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL",
a move consists of either replacing one occurrence of "XL" with "LX",
or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end,
return True if and only if there exists a sequence of moves to transform one string to the other.

Example:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: True

Explanation:
We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX
'''
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        '''
        Only 2 possible conversion
        XL => LX
        RX => XR
        '''
        rCount = 0 # 'R' count from start
        lCount = 0 # 'L' count from end
        for i in range(len(start)):
            cs = start[i]
            ce = end[i]
            if cs != ce:                        
                if cs == 'L':
                    if ce == 'X' and lCount > 0:
                        # 'L' in start can only move to left
                        lCount -= 1
                    else: # ce == 'R' or lCount == 0
                        return False
                elif cs == 'R':
                    if ce == 'X':
                        # 'R' in start can only move to right
                        rCount += 1
                    else: # ce == 'L'
                        return False
                else: # cs == 'X'
                    if ce == 'L':
                        lCount += 1
                    elif ce == 'R' and rCount > 0:
                        rCount -= 1
                    else:
                        return False
                        
        return rCount == 0 and lCount == 0
                
