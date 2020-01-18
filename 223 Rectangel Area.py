'''
223. Rectangle Area
https://leetcode.com/problems/rectangle-area/

Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Rectangle Area

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
'''
from typing import Tuple

class Solution:
    def overlappedInterval(self, i1: Tuple[int, int], i2: Tuple[int, int]) -> int:
        '''
        Return the overlapped length of 2 intervals
        '''
        return max(0, min(i1[1], i2[1]) - max(i1[0], i2[0]))
        
    def overlappedArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        return self.overlappedInterval((A, C), (E, G)) * self.overlappedInterval((B, D), (F, H))
        
    def rectangleArea(self, A: int, B: int, C: int, D: int) -> int:
        return abs((A-C) * (B-D))
        
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        return self.rectangleArea(A,B,C,D) + self.rectangleArea(E,F,G,H) - self.overlappedArea(A,B,C,D,E,F,G,H)
