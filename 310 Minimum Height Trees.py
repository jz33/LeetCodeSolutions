'''
Minimum Height Trees
https://leetcode.com/problems/minimum-height-trees/
'''
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # Construct tree
        graph = {}
        for i in xrange(n):
            graph[i] = set()
        for pair in edges:
            x = pair[0]
            y = pair[1]
            graph[x].add(y)
            graph[y].add(x)
        
        for k,v in graph.iteritems(): print k, list(v)
        
        # Remove leaves bfs
        leaves = [i for i in xrange(0,n) if len(graph[i]) <= 1]
        n -= len(leaves)
        while n > 0:
            newLeaves = []
            for leaf in leaves:
                parent = graph[leaf].pop()
                graph[parent].discard(leaf)
                if len(graph[parent]) == 1:
                    newLeaves.append(parent)
                del graph[leaf]
            leaves = newLeaves
            n -= len(leaves)  
        return leaves
        
sol = Solution()
n = 7
edges = [[0, 1], [0, 2], [1, 3], [4, 1], [5, 2], [6, 2]]
print sol.findMinHeightTrees(n,edges)
