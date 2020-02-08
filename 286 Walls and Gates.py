'''
286. Walls and Gates
https://leetcode.com/problems/walls-and-gates/

You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as
you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate,
it should be filled with INF.

Example: 

Given the 2D grid:

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
  
After running your function, the 2D grid should be:

  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
'''
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or not rooms[0]:
            return
        
        rowCount = len(rooms)
        colCount = len(rooms[0])

        def mark(x,y):
            queue = collections.deque([(x,y)])
            steps = 1
            while queue:
                for _ in range(len(queue)):
                    x,y = queue.popleft()
                    for i,j in (x,y+1), (x,y-1), (x+1,y), (x-1,y):
                        if 0 <= i < rowCount and 0 <= j < colCount and rooms[i][j] > steps:
                            rooms[i][j] = steps
                            queue.append((i,j))
                steps += 1
        
        for i in range(rowCount):
            for j in range(colCount):
                if rooms[i][j] == 0:
                    mark(i,j)
