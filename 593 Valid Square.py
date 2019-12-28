'''
593. Valid Square
https://leetcode.com/problems/valid-square/

Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True

Note:

    All the input integers are in the range [-10000, 10000].
    A valid square has four equal sides with positive length and four equal angles (90-degree angles).
    Input points have no order.

'''
from math import sqrt, isclose

def euclidean(p1, p2) -> float:
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
    
def dot(p1, p2, p3) -> int:
    # p2 is in center
    v1 = [p1[0] - p2[0], p1[1] - p2[1]]
    v2 = [p3[0] - p2[0], p3[1] - p2[1]]
    return v1[0] * v2[0] + v1[1] * v2[1]
    
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        '''
        1. Start 1st point. Find its 2 neighbor points and 1 diagnal point by
        computing Euclidean distances
        '''
        dist12 = euclidean(p1, p2)
        if isclose(dist12, 0):
            # Duplicate points
            return False
        
        dist13 = euclidean(p1, p3)
        if isclose(dist13, 0):
            return False
        
        dist14 = euclidean(p1, p4)
        if isclose(dist14, 0):
            return False
        
        diagnal = None
        neighbors = []
        if isclose(dist12, dist13) and isclose(sqrt(2) * dist12, dist14):
            diagnal = p4
            neighbors = [p2, p3]
        elif isclose(dist12, dist14) and isclose(sqrt(2) * dist12, dist13):
            diagnal = p3
            neighbors = [p2, p4]
        elif isclose(dist13, dist14) and isclose(sqrt(2) * dist13, dist12):
            diagnal = p2
            neighbors = [p3, p4]
        
        if diagnal is None:
            return False
        
        '''
        2. Check angles using dot product. Angle is 90 degree, dot product should be 0
        '''
        return dot(p1, neighbors[0], diagnal) == 0 and \
               dot(p1, neighbors[1], diagnal) == 0 and \
               dot(neighbors[0], diagnal, neighbors[1]) == 0 and \
               dot(neighbors[0], p1, neighbors[1]) == 0 
