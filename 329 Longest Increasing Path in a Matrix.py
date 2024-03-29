'''
329. Longest Increasing Path in a Matrix
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down.
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

Example 1:

Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:

Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:

Input: matrix = [[1]]
Output: 1

Constraints:
    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 200
    0 <= matrix[i][j] <= 231 - 1
'''
class Solution:
    '''
    Time Complexity: each vertex and edges are visited exactly once,
    then O(V+E) = O(m*n)
    '''
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rowCount = len(matrix)
        colCount = len(matrix[0])
        
        # seen[i][j] records the longest increasing path size on (i,j)
        seen = [[1] * colCount for _ in range(rowCount)]
        
        def bfs(start):
            queue = deque([start])
            size = 2
            while queue:
                for _ in range(len(queue)):
                    i, j = queue.popleft()
                    for x, y in (i, j+1), (i, j-1), (i+1, j), (i-1, j):
                        if 0 <= x < rowCount and 0 <= y < colCount and matrix[x][y] > matrix[i][j] and size > seen[x][y]:
                            seen[x][y] = size
                            queue.append((x, y))
                size += 1
            
        for i in range(rowCount):
            for j in range(colCount):
                if seen[i][j] == 1:
                    bfs((i,j))

        return max(seen[i][j] for i in range(rowCount) for j in range(colCount))
