'''
261. Graph Valid Tree
https://leetcode.com/problems/graph-valid-tree/

You have a graph of n nodes labeled from 0 to n - 1.
You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that
there is an undirected edge between nodes ai and bi in the graph.

Return true if the edges of the given graph make up a valid tree, and false otherwise.

Example 1:

Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

Example 2:

Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false

Constraints:
    1 <= n <= 2000
    0 <= edges.length <= 5000
    edges[i].length == 2
    0 <= ai, bi < n
    ai != bi
    There are no self-loops or repeated edges.
'''
class UnionFind:
    def __init__(self, nodeCount: int):
        self.tree = list(range(nodeCount))

    def find(self, node: int) -> int:
        tree = self.tree
        if tree[node] != node:
            tree[node] = self.find(tree[node])
        return tree[node]
    
    def union(self, nodeX: int, nodeY: int) -> bool:
        rootX = self.find(nodeX)
        rootY = self.find(nodeY)
        if rootX != rootY:
            self.tree[rootX] = rootY
            return True
        return False
            
    def rootCount(self) -> int:
        return sum(self.tree[node] == node for node in range(len(self.tree)))
    
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        To tell if an undirected graph is a valid tree:
        1. The graph must be connected 
        2. The graph must have no redundant edge
        '''
        graph = UnionFind(n)
        return all(graph.union(edge[0], edge[1]) for edge in edges) and graph.rootCount() == 1
