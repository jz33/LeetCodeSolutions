'''
286. Walls and Gates
https://leetcode.com/problems/walls-and-gates/

You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that
the distance to a gate is less than 2147483647.

Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

Example 1:

Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

Example 2:

Input: rooms = [[-1]]
Output: [[-1]]

Constraints:
    m == rooms.length
    n == rooms[i].length
    1 <= m, n <= 250
    rooms[i][j] is -1, 0, or 231 - 1.
'''
GATE = 0

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        rowCount = len(rooms)
        colCount = len(rooms[0])

        def bfs(start):
            queue = [start]
            steps = 1
            while queue:
                newQueue = []
                for x, y in queue:
                    for i, j in (x,y+1), (x,y-1), (x+1,y), (x-1,y):
                        if 0 <= i < rowCount and 0 <= j < colCount and rooms[i][j] > steps:
                            rooms[i][j] = steps
                            newQueue.append((i,j))
                steps += 1
                queue = newQueue                
        
        for i in range(rowCount):
            for j in range(colCount):
                if rooms[i][j] == GATE:
                    bfs((i,j))
