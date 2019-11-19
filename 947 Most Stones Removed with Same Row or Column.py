'''
947. Most Stones Removed with Same Row or Column
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

On a 2D plane, we place stones at some integer coordinate points.  Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or row with another stone on the grid.

What is the largest possible number of moves we can make?

Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5

Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3

Example 3:

Input: stones = [[0,0]]
Output: 0
'''
from typing import Tuple

class UnionFind:
    def __init__(self, stones: List[List[int]]):
        self.nodes = {} # dict of tuples
        for x, y in stones:
            tup = (x, y)
            self.nodes[tup] = tup
    
    def Find(self, i: Tuple[int]) -> Tuple[int]:
        nodes = self.nodes        
        if nodes[i] != i:
            nodes[i] = self.Find(nodes[i])
        return nodes[i]
    
    def Union(self, i: Tuple[int], j: Tuple[int]):
        ri = self.Find(i)
        rj = self.Find(j)      
        if ri != rj:
            self.nodes[rj] = ri

    def RootCount(self) -> int:
        return sum(self.nodes[n] == n for n in self.nodes.keys())

class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        rows = collections.defaultdict(list) # row index : [column index]
        cols = collections.defaultdict(list)
        for stone in stones:
            rows[stone[0]].append(stone[1])
            cols[stone[1]].append(stone[0])

        graph = UnionFind(stones)
        for i, row in rows.items():
            for j in range(1, len(row)):
                graph.Union((i,row[j-1]), (i,row[j]))

        for i, col in cols.items():
            for j in range(1, len(col)):
                graph.Union((col[j-1],i), (col[j],i))

        return len(stones) - graph.RootCount()
