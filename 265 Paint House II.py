'''
Paint House II
https://leetcode.com/problems/paint-house-ii/

There are a row of n houses, each house can be painted with one of the k colors.
The cost of painting each house with a certain color is different.
You have to paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k cost matrix.
For example, costs[0][0] is the cost of painting house 0 with color 0; costs[1][2] is the cost of
painting house 1 with color 2, and so on... Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[1,5,3],[2,9,4]]
Output: 5
Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum cost: 1 + 4 = 5; 
             Or paint house 0 into color 2, paint house 1 into color 0. Minimum cost: 3 + 2 = 5. 
Follow up:
Could you solve it in O(nk) runtime?
'''
class TwinMins:
    '''
    A class manages the 1st minimun and 2nd minimun values
    '''
    def __init__(self):
        # m0 <= m1
        self.m0 = None
        self.m1 = None
        
    def setMin(self, i, v):
        # Be careful about the order here!
        if self.m0 is None:
            self.m0 = (i, v)
        elif v <= self.m0[1]:
            self.m0, self.m1 = (i, v), self.m0
        elif self.m1 is None:
            self.m1 = (i, v)      
        elif v < self.m1[1]:
            self.m1 = (i, v)
            
    def update(self, i, v, prev):
        if i == prev.m0[0]:
            self.setMin(i, v + prev.m1[1])
        else:
            self.setMin(i, v + prev.m0[1])
            
    def __repr__(self):
        return str(self.m0) + " " + str(self.m1)
                
class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        rowCount = len(costs)
        if not rowCount:
            return 0
        
        colCount = len(costs[0])
        if colCount == 0:
            return 0
        if colCount == 1:
            return costs[0][0] if rowCount == 1 else 0 
                
        tw = TwinMins()
        for i in range(colCount):
            tw.setMin(i, costs[0][i])
        
        for i in range(1,rowCount):
            ntw = TwinMins()
            for j in range(colCount):
                ntw.update(j, costs[i][j], tw)
            tw = ntw
            
        return tw.m0[1]
