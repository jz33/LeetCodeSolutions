'''
85 Maximal Rectangle
https://leetcode.com/problems/maximal-rectangle

Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
'''
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:        
        heights = [0] + heights + [0] # just to make code simpler
        stack = [0] # record indexes, where heights are increasing
        maxRec = 0
        for i, h in enumerate(heights):
            while h < heights[stack[-1]]:
                j = stack.pop()
                recHeight = heights[j]
                # recHeight is the target rectangle's height, 
                # its right is before i, its left is after stack[-1], 
                # all heights between stack[-1] and j (even not in stack)
                # should be equal or larger than recHeight
                maxRec = max(maxRec, (i-1-stack[-1]) * recHeight)
            stack.append(i)
        return maxRec

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        '''
        Cannot use DP method of 221. Maximal Square
        Use 84 Largest Rectangle in Histogram.
        '''
        rowCount = len(matrix)
        if not rowCount:
            return 0
        colCount = len(matrix[0])
        if not colCount:
            return 0
        
        heights = [0] * colCount  
        maxArea = 0
        for i in range(rowCount):
            for j in range(colCount):
                heights[j] = 0 if matrix[i][j] == '0' else heights[j] + 1
            maxArea = max(maxArea, self.largestRectangleArea(heights))
            
        return maxArea
