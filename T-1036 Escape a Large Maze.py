'''
1036. Escape a Large Maze
https://leetcode.com/problems/escape-a-large-maze/

In a 1 million by 1 million grid, the coordinates of each grid square are (x, y) with 0 <= x, y < 10^6.

We start at the source square and want to reach the target square.  Each move, we can walk to a 4-directionally adjacent square in the grid that isn't in the given list of blocked squares.

Return true if and only if it is possible to reach the target square through a sequence of moves.

Example 1:

Input: blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
Output: false
Explanation: 
The target square is inaccessible starting from the source square, because we can't walk outside the grid.

Example 2:

Input: blocked = [], source = [0,0], target = [999999,999999]
Output: true
Explanation: 
Because there are no blocked cells, it's possible to reach the target square.

Note:

    0 <= blocked.length <= 200
    blocked[i].length == 2
    0 <= blocked[i][j] < 10^6
    source.length == target.length == 2
    0 <= source[i][j], target[i][j] < 10^6
    source != target
'''
from collections import deque
from typing import Tuple
from enum import Enum, auto

class Result(Enum):
    Connected = auto() # If target and source are connected
    Blocked = auto()# If the source node is blocked by blocks
    MaxLevelReached = auto()

class Solution:
    def bfs(self, src: Tuple[int], tag: Tuple[int]):
        blocks = self.blocks
        bound = self.bound
        
        visited = set()
        visited.add(src)
        queue = deque()
        queue.append(src)
        level = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == tag:
                    return Result.Connected
                
                x,y = node
                for i,j in [(x+1,y), (x-1, y), (x,y+1), (x,y-1)]:
                    if 0 <= i <= 1000000 and 0 <= j <= 1000000 and (i,j) not in visited and (i,j) not in blocks:
                        queue.append((i,j))
                        visited.add((i,j))
            level += 1
            if level == bound:
                break
        else:
            return Result.Blocked
        
        return Result.MaxLevelReached        
    
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if not blocked:
            return True
        
        self.blocks = set(map(tuple, blocked))
        
        # The maximun levels need to perform on BFS
        self.bound = len(self.blocks)
        
        res = self.bfs(tuple(source), tuple(target))
        if res == Result.Blocked:
            return False
        elif res == Result.Connected:
            return True
        else:
            return False if self.bfs(tuple(target), tuple(source)) == Result.Blocked else True
