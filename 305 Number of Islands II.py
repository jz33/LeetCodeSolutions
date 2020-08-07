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
class UnionFind:
    def __init__(self):
        self.tree = {}
        # For performance, do not count root from tree for perform
        self.rootCount = 0

    def find(self, node):
        tree = self.tree
        if tree[node] != node:
            tree[node] = self.find(tree[node])
        return tree[node]
    
    def union(self, node):
        '''
        The uniqueness of this union find problem is here:
        for performance, union 4 neighbors together.
        '''
        tree = self.tree
        
        # Get all unique roots from neighbor
        x, y = node
        roots = set()
        for neighbor in [(x, y+1), (x, y-1), (x+1, y), (x-1, y)]:
            if neighbor in tree:
                roots.add(self.find(neighbor))
        
        # Just set all neighbor's root to current node
        for root in roots:
            tree[root] = node
        
        # Set current node's root as self
        tree[node] = node
        
        # All neighbors + current node are going to be unioned as one
        self.rootCount += 1 - len(roots)
        
class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        result = []
        graph = UnionFind()
        for x, y in positions:
            node = (x, y)
            if node in graph.tree:
                result.append(result[-1])
            else:
                graph.union(node)
                result.append(graph.rootCount)
                
        return result
