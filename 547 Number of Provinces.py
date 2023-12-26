'''
547. Number of Provinces
https://leetcode.com/problems/number-of-provinces/

There are n cities. Some of them are connected, while some are not.
If city a is connected directly with city b, and city b is connected directly with city c,
then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if
the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2

Example 2:

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

Constraints:
    1 <= n <= 200
    n == isConnected.length
    n == isConnected[i].length
    isConnected[i][j] is 1 or 0.
    isConnected[i][i] == 1
    isConnected[i][j] == isConnected[j][i]
'''
class UnionFind:
    def __init__(self, count: int):
        self.tree = list(range(count))

    def find(self, node):
        tree = self.tree
        if tree[node] != node:
            tree[node] = self.find(tree[node])
        return tree[node]
    
    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra != rb:
            self.tree[ra] = rb

    def rootCount(self) -> int:
        return sum(k == v for k, v in enumerate(self.tree))

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        count = len(isConnected)
        if not count:
            return 0
        
        graph = UnionFind(count)
        for i in range(count):
            for j in range(i + 1, count):
                if isConnected[i][j] == 1:
                    graph.union(i, j)
        
        return graph.rootCount()
