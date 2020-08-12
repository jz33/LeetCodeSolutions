'''
329. Longest Increasing Path in a Matrix
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down.
You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
  
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rowCount = len(matrix)
        colCount = len(matrix[0])
        
        # seen[i][j] records the longest increasing path size on (i,j)
        seen = [[1] * colCount for _ in range(rowCount)]
        
        def bfs(a: int, b: int):
            stack = [(a, b)]
            size = 2
            while stack:
                newStack = []
                for i, j in stack:
                    for x, y in (i, j+1), (i, j-1), (i+1, j), (i-1, j):
                        if 0 <= x < rowCount and 0 <= y < colCount and matrix[x][y] > matrix[i][j] and size > seen[x][y]:
                            seen[x][y] = size
                            newStack.append((x, y))
                size += 1
                stack = newStack
            
        for i in range(rowCount):
            for j in range(colCount):
                if seen[i][j] == 1:
                    bfs(i, j)

        return max(seen[i][j] for i in range(rowCount) for j in range(colCount))
