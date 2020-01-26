'''
305. Number of Islands II
https://leetcode.com/problems/number-of-islands-ii/

A 2d grid map of m rows and n columns is initially filled with water.
We may perform an addLand operation which turns the water at position (row, col) into a land.
Given a list of positions to operate, count the number of islands after each addLand operation.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.

Example:

Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]
Explanation:

Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
Follow up:

Can you do it in time complexity O(k log mn), where k is the length of the positions?
'''
from typing import Tuple

class Solution:
    def getParent(self, node: Tuple[int,int]) -> Tuple[int,int]:
        tree = self.tree
        while node in tree and tree[node] != node:
            node = tree[node]
        return node
    
    def union(self, start) -> int:
        tree = self.tree
        
        # 1. Find root of all 4 neighbors
        roots = set()
        i,j = start
        for neighbor in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
            if neighbor in tree:
                roots.add(self.getParent(neighbor))

        rootsCount = len(roots)
        if not roots:
            tree[start] = start
        else:
            root = roots.pop()
            for nr in roots:
                tree[nr] = root
            tree[start] = root
            
        return rootsCount
    
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        self.tree = {} # Union Find tree, {point : parent point}
        counts = []
        for positions in positions:
            point = (positions[0], positions[1])
            previousCount = 0 if not counts else counts[-1]
            
            if point not in self.tree: 
                rootsCount = self.union(point)
                counts.append(previousCount + 1 - rootsCount)
            else:
                counts.append(previousCount)
                
        return counts
