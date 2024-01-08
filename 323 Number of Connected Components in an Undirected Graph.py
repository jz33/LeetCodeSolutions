'''
323. Number of Connected Components in an Undirected Graph
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

You have a graph of n nodes.
You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that
there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

Example 1:

Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Example 2:

Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1

Constraints:
    1 <= n <= 2000
    1 <= edges.length <= 5000
    edges[i].length == 2
    0 <= ai <= bi < n
    ai != bi
    There are no repeated edges.
'''
class UnionFind:
    def __init__(self, nodeCount: int):
        self.tree = list(range(nodeCount))

    def find(self, node: int) -> int:
        tree = self.tree
        if tree[node] != node:
            tree[node] = self.find(tree[node])
        return tree[node]
    
    def union(self, nodeX: int, nodeY: int):
        rootX = self.find(nodeX)
        rootY = self.find(nodeY)
        if rootX != rootY:
            self.tree[rootX] = rootY
            
    def rootCount(self) -> int:
        return sum(self.tree[node] == node for node in range(len(self.tree)))
    
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = UnionFind(n)
        for x, y in edges:
            graph.union(x, y)
        return graph.rootCount()
