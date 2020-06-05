'''
1102. Path With Maximum Minimum Value
https://leetcode.com/problems/path-with-maximum-minimum-value/

Given a matrix of integers A with R rows and C columns, find the maximum score of a path starting at [0,0] and ending at [R-1,C-1].

The score of a path is the minimum value in that path.  For example, the value of the path 8 →  4 →  5 →  9 is 4.

A path moves some number of times from one visited cell to any neighbouring unvisited cell in one of
the 4 cardinal directions (north, east, west, south).

Example 1:

Input: [[5,4,5],[1,2,6],[7,4,6]]
Output: 4

Explanation: 
The path with the maximum score is highlighted in yellow. 

Example 2:

Input: [[2,2,1,2,2,2],[1,2,2,2,1,2]]
Output: 2

Example 3:

Input: [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
Output: 3
'''
from heapq import heappush, heappop

class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        '''
        Dijkstra
        '''
        if not A or not A[0]:
            return 0
        
        rowCount = len(A)
        colCount = len(A[0])
        
        heap = [(-A[0][0], 0, 0)] # max heap, (score, x, y)
        
        # Why not record path score too? Because Dijkstra algorithm is greedy,
        # for any cell, firt time visiting should already have the lowest score
        visited = {(0, 0)} # W
        
        while heap:
            s, i, j = heappop(heap)
            s = -s
            if i == rowCount -1 and j == colCount - 1:
                return s
            
            for x, y in (i, j+1), (i, j-1), (i+1, j), (i-1, j):
                if 0 <= x < rowCount and 0 <= y < colCount and (x, y) not in visited:
                    visited.add((x,y))
                    heappush(heap, (-min(A[x][y], s), x ,y))
        
        return 0
