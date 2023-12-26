'''
2421. Number of Good Paths
https://leetcode.com/problems/number-of-good-paths/

There is a tree (i.e. a connected, undirected graph with no cycles) consisting of
n nodes numbered from 0 to n - 1 and exactly n - 1 edges.

You are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node.
You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that
there exists an undirected edge connecting nodes ai and bi.

A good path is a simple path that satisfies the following conditions:

The starting node and the ending node have the same value.

All nodes between the starting node and the ending node have values less than or equal to
the starting node (i.e. the starting node's value should be the maximum value along the path).

Return the number of distinct good paths.

Note that a path and its reverse are counted as the same path.
For example, 0 -> 1 is considered to be the same as 1 -> 0.
A single node is also considered as a valid path.

Example 1:

Input: vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]
Output: 6
Explanation: There are 5 good paths consisting of a single node.
There is 1 additional good path: 1 -> 0 -> 2 -> 4.
(The reverse path 4 -> 2 -> 0 -> 1 is treated as the same as 1 -> 0 -> 2 -> 4.)
Note that 0 -> 2 -> 3 is not a good path because vals[2] > vals[0].

Example 2:

Input: vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]
Output: 7
Explanation: There are 5 good paths consisting of a single node.
There are 2 additional good paths: 0 -> 1 and 2 -> 3.

Example 3:

Input: vals = [1], edges = []
Output: 1
Explanation: The tree consists of only one node, so there is one good path.

Constraints:
    n == vals.length
    1 <= n <= 3 * 104
    0 <= vals[i] <= 105
    edges.length == n - 1
    edges[i].length == 2
    0 <= ai, bi < n
    ai != bi
    edges represents a valid tree.
'''
from typing import List

class UnionFind:
    def __init__(self, vals: List[int]):
        # The normal union find tree
        self.tree = list(range(len(vals)))
        # A special map for this question
        # It contains each node's root's max value and count
        self.maxNodes = [(val, 1) for val in vals] # [(max value, count)]
        
    def find(self, node: int) -> int:
        tree = self.tree
        if tree[node] != node:
            tree[node] = self.find(tree[node])
        return tree[node]
    
    def union(self, maxVal: int, nodeA: int, nodeB: int) -> int:
        '''
        @maxVal: the max val of the 2 values of node A & B
        Union 2 nodes, update max nodes, return good path increment
        '''
        rootA = self.find(nodeA)
        rootB = self.find(nodeB)
        # No need to check rootA != rootB as the tree is valid,
        # i.e, new edge always connects 2 sections
        self.tree[rootB] = rootA

        maxNodes = self.maxNodes

        # The max val node count of the tree of A can be 0 if no existing nodes of tree A has max val;
        # (they must have lesser valued nodes); or non-0 if there were previous nodes of tree A has the max val
        maxValCountA = maxNodes[rootA][1] if maxNodes[rootA][0] == maxVal else 0
        maxValCountB = maxNodes[rootB][1] if maxNodes[rootB][0] == maxVal else 0

        # Update the max nodes val + count of the nodes
        maxNodes[rootA] = (maxVal, maxValCountA + maxValCountB)
        maxNodes[rootB] = (maxVal, maxValCountA + maxValCountB)

        # A new edge of A & B connects the 2 tree, and any node with max value in tree A
        # can make a good path to any node with max value in tree B.
        # Therefore newly added good paths are maxValCountA * maxValCountB
        return maxValCountA * maxValCountB

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        tree = UnionFind(vals)
    
        # [(max val of fromNode or toNode, fromNode, toNode)]
        # Add the edge in order from starting values 
        maxValEdges = sorted((max(vals[fromNode], vals[toNode]),fromNode,toNode) for fromNode, toNode in edges)

        # All single nodes are good paths
        result = len(vals)
        for maxVal, nodeA, nodeB in maxValEdges:
            result += tree.union(maxVal, nodeA, nodeB)

        return result
    
sol = Solution()
vals = [1,3,2,1,3]
edges = [[0,1],[0,2],[2,3], [2,4]]
print(sol.numberOfGoodPaths(vals, edges))