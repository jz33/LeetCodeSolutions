'''
323. Number of Connected Components in an Undirected Graph
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
'''
class UnionFind:
    def __init__(self, nodeCount: int):
        self.tree = list(range(nodeCount))

    def find(self, node: int) -> int:
        tree = self.tree
        if tree[node] != node:
            tree[node] = self.find(tree[node])
        return tree[node]
    
    def union(self, x: int, y: int):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            self.tree[rx] = ry
            
    def rootCount(self) -> int:
        return sum(self.tree[node] == node for node in range(len(self.tree)))
    
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = UnionFind(n)
        for x, y in edges:
            graph.union(x, y)
        return graph.rootCount()
