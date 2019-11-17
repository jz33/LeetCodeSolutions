'''
261. Graph Valid Tree
https://leetcode.com/problems/graph-valid-tree/

Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes),
    write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false

Note: you can assume that no duplicate edges will appear in edges. Since all edges are undirected,
    [0,1] is the same as [1,0] and thus will not appear together in edges.
'''
class UnionFind:
    def __init__(self, nodeCount: int):
        self.nodes = list(range(nodeCount))
    
    def Find(self, i: int):
        nodes = self.nodes
        if nodes[i] != i:
            nodes[i] = self.Find(nodes[i])
        return nodes[i]
    
    def Union(self, i: int, j: int) -> bool:
        ri = self.Find(i)
        rj = self.Find(j)
        if ri == rj:
            return False
        self.nodes[ri] = rj
        return True
    
    def RootCount(self):
        nodes = self.nodes
        return sum(nodes[i] == i for i in range(len(nodes)))
        
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        To tell if an undirected graph is a valid tree:
        1. The graph must be connected 
        2. The graph must have no redundant edge
        '''
        graph = UnionFind(n)
        return all(graph.Union(edge[0], edge[1]) for edge in edges) and graph.RootCount() == 1
