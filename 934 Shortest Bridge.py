'''
934. Shortest Bridge
https://leetcode.com/problems/shortest-bridge/

In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)

Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)

Example 1:

Input: [[0,1],[1,0]]
Output: 1

Example 2:

Input: [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Example 3:

Input: [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
'''
from typing import Tuple

ISLAND_1 = -1
ISLAND_2 = -1

class FixedQueue:
    '''
    The left side of this queue is fixed
    '''
    def __init__(self):
        self.data = []
        self.i = 0 # left element index
    
    def add(self, e):
        self.data.append(e)
        
    def hasNext(self) -> bool:
        return self.i < len(self.data)
    
    def size(self) -> int:
        return len(self.data) - self.i
    
    def pop(self):
        '''
        Not actually pop the data
        '''
        e = self.data[self.i]
        self.i += 1
        return e
        
    def reset(self):
        self.i = 0
        return self
    
    def __repr__(self):
        return str(self.i) + " " + str(self.data)

class Solution:
    def getIslandPoints(self, A: List[List[int]]):
        for i in range(self.rowCount):
            for j in range(self.colCount):
                if A[i][j] == 1:                 
                    queue = FixedQueue()
                    queue.add((i,j))
                    A[i][j] = ISLAND_1
                    while queue.hasNext():
                        a,b = queue.pop()
                        for d in [(0,1), (1,0), (-1,0), (0,-1)]:
                            x, y = a + d[0], b + d[1]
                            if 0 <= x < self.rowCount and 0 <= y < self.colCount and A[x][y] == 1:
                                A[x][y] = ISLAND_1
                                queue.add((x,y))
                    return queue.reset()
        return None
        
    def shortestBridge(self, A: List[List[int]]) -> int:
        self.rowCount = len(A)
        self.colCount = len(A[0])
        
        # Get all points of first island
        queue = self.getIslandPoints(A)
        
        # BFS
        dist = 0
        while queue.hasNext():
            for _ in range(queue.size()):
                i,j = queue.pop()
                for d in [(0,1), (1,0), (-1,0), (0,-1)]:
                    x, y = i + d[0], j + d[1]
                    if 0 <= x < self.rowCount and 0 <= y < self.colCount and A[x][y] != ISLAND_1:
                        if A[x][y] == 1:
                            return dist
                        
                        A[x][y] = ISLAND_1
                        queue.add((x,y))
            dist += 1
        return -1
