'''
490. The Maze
https://leetcode.com/problems/the-maze/

There is a ball in a maze with empty spaces and walls.
The ball can go through empty spaces by rolling up, down, left or right, but it won't stop rolling until hitting a wall.
When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space.
You may assume that the borders of the maze are all walls.
The start and destination coordinates are represented by row and column indexes.

Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: true

Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: false

Explanation: There is no way for the ball to stop at the destination.

Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures),
but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.
'''
from heapq import heappush, heappop

class Solution:
    def getNexts(self, maze, start):
        '''
        Return list of next reachable nodes and the cost to reach there from start
        '''
        res = []
        for direction in [(0,1), (1,0), (0,-1), (-1,0)]:
            cost = 0
            i,j = start[0], start[1]
            while True:
                x, y = i + direction[0], j + direction[1]
                if 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != 1:
                    cost += 1
                    i,j = x,y
                else:
                    break
            if cost != 0:
                res.append([(i,j), cost])
        return res
    
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        s = (start[0], start[1])
        d = (destination[0], destination[1])
        visited = {s : 0} # {visited node : total cost to reach node}
        heap = [(0, s)] # [total cost, node]
        while heap:
            sofarCost, node = heappop(heap)
            if node == d:
                return True          
            for nx, cost in self.getNexts(maze, node):
                if nx not in visited or visited[nx] > cost + sofarCost:
                    nextCost = cost + sofarCost
                    heappush(heap, (nextCost, nx))
                    visited[nx] = nextCost                 
        return False
