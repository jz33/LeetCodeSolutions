'''
959. Regions Cut By Slashes
https://leetcode.com/problems/regions-cut-by-slashes/

In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \, or blank space.
These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a \ is represented as "\\".)

Return the number of regions.

Example 1:

Input:
[
  " /",
  "/ "
]
Output: 2
Explanation: The 2x2 grid is as follows:

Example 2:

Input:
[
  " /",
  "  "
]
Output: 1
Explanation: The 2x2 grid is as follows:

Example 3:

Input:
[
  "\\/",
  "/\\"
]
Output: 4
Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/, and "/\\" refers to /\.)
The 2x2 grid is as follows:

Example 4:

Input:
[
  "/\\",
  "\\/"
]
Output: 5
Explanation: (Recall that because \ characters are escaped, "/\\" refers to /\, and "\\/" refers to \/.)
The 2x2 grid is as follows:

Example 5:

Input:
[
  "//",
  "/ "
]
Output: 3
Explanation: The 2x2 grid is as follows:

Note:

1 <= grid.length == grid[0].length <= 30
grid[i][j] is either '/', '\', or ' '.
'''
from typing import Tuple

class UnionFind:
    def __init__(self):
        self.parents = {}
    
    def add(self, node: Tuple[int]):
        self.parents[node] = node

    def find(self, node: Tuple[int]) -> Tuple[int]:
        ps = self.parents
        if ps[node] != node:
            ps[node] = self.find(ps[node])
        return ps[node]
    
    def union(self, a: Tuple[int], b: Tuple[int]):
        ra = self.find(a)
        rb = self.find(b)
        if ra != rb:
            self.parents[ra] = rb

    def rootCount(self) -> int:
        ps = self.parents
        return sum(ps[node] == node for node in ps)
    
class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        if not grid or not grid[0]:
            return 0
        rowCount = len(grid)
        colCount = len(grid[0])
        
        graph = UnionFind()
        
        # Notation of the node:
        # if cell(i, j) is " ", node is (i, j);
        # if cell(i, j) is "/", nodes are (i, j, 1), (i, j, 2);
        # if cell(i, j) is "\", nodes are (i, j, 3), (i, j, 4)
        
        def unionNeighbours(node1: Tuple[int], node2: Tuple[int], x: int, y: int):
            '''
            @node1: the node who is going to be unioned with upper neighbor
            @node2: the node who is going to be unioned with left neighbor
            '''
            if x > 0:
                # Union upper neighbour
                if grid[x-1][y] == ' ':
                    graph.union(node1, (x-1, y))
                elif grid[x-1][y] == '/':
                    graph.union(node1, (x-1, y, 2))
                else:
                    graph.union(node1, (x-1, y, 3))
            
            if y > 0:
                # Union left neighbor
                if grid[x][y-1] == ' ':
                    graph.union(node2, (x, y-1))
                elif grid[x][y-1] == '/':
                    graph.union(node2, (x, y-1, 2))
                else:
                    graph.union(node2, (x, y-1, 4))
        
        # At current cell, only try union with top cell and left cell
        for i in range(rowCount):
            for j in range(colCount):
                if grid[i][j] == ' ':
                    node = (i, j)
                    graph.add(node)
                    unionNeighbours(node, node, i, j)
                elif grid[i][j] == '/':
                    node1 = (i, j, 1)
                    node2 = (i, j, 2)
                    graph.add(node1)
                    graph.add(node2)
                    unionNeighbours(node1, node1, i, j)
                else: # grid[i][j] == '\'
                    node3 = (i, j, 3)
                    node4 = (i, j, 4)
                    graph.add(node3)
                    graph.add(node4)
                    unionNeighbours(node4, node3, i, j)
                    
        return graph.rootCount()        
