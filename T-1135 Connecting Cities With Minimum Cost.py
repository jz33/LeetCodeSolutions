'''
Connecting Cities With Minimum Cost
https://leetcode.com/problems/connecting-cities-with-minimum-cost/

There are N cities numbered from 1 to N.

You are given connections, where each connections[i] = [city1, city2, cost] represents the cost to connect city1 and city2 together.
(A connection is bidirectional: connecting city1 and city2 is the same as connecting city2 and city1.)

Return the minimum cost so that for every pair of cities, there exists a path of connections (possibly of length 1) that
connects those two cities together.  The cost is the sum of the connection costs used.

If the task is impossible, return -1.

Example 1:

Input: N = 3, connections = [[1,2,5],[1,3,6],[2,3,1]]
Output: 6
Explanation: 
Choosing any 2 edges will connect all cities so we choose the minimum 2.

Example 2:

Input: N = 4, connections = [[1,2,3],[3,4,4]]
Output: -1
Explanation: 
There is no way to connect all cities even if all edges are used.
'''
class UnionFind:
    def __init__(self, nodeCount : int):
        # Initialize parent tree, [0] is not used
        self.parents = list(range(nodeCount + 1))
    
    def find(self, node: int) -> int:
        ps = self.parents
        if ps[node] != node:
            ps[node] = self.find(ps[node])
        return ps[node]
    
    def union(self, a: int, b: int) -> bool:
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False  
        self.parents[ra] = rb
        return True

class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        if N == 0:
            return 0
 
        # Sort by cost
        connections.sort(key = lambda x : x[2])
        
        graph = UnionFind(N)
        edges = 0
        costs = 0
        for f, t, c in connections:
            if graph.union(f, t):
                edges += 1
                costs += c
                
            if edges == N - 1:
                return costs
        
        return -1
