'''
1245. Tree Diameter
https://leetcode.com/problems/tree-diameter/

Given an undirected tree, return its diameter: the number of edges in a longest path in that tree.

The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge between nodes u and v.
Each node has labels in the set {0, 1, ..., edges.length}.

Example 1:

Input: edges = [[0,1],[0,2]]
Output: 2
Explanation: 
A longest path of the tree is the path 1 - 0 - 2.

Example 2:

Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
Output: 4
Explanation: 
A longest path of the tree is the path 3 - 2 - 1 - 4 - 5.

Constraints:

0 <= edges.length < 10^4
edges[i][0] != edges[i][1]
0 <= edges[i][j] <= edges.length
The given edges form an undirected tree.
'''
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        if not edges:
            return 0
        
        graph = {} # { node : [nodes]}
        for f, t in edges:
            graph[f] = graph.get(f, []) + [t]
            graph[t] = graph.get(t, []) + [f]

        maxNodeCount = 1

        def postorder(node: int, parent: int) -> int:
            '''
            @return: max node count from node to 1 of its child branch.
            Similar to 124. Binary Tree Maximum Path Sum
            '''
            nonlocal maxNodeCount
            singlePaths = [] # maximum path count of children
            for togo in graph[node]:
                if togo != parent:
                    singlePaths.append(postorder(togo, node))
            
            if not singlePaths:
                return 1
            
            if len(singlePaths) == 1:
                nodeCount = 1 + singlePaths[0]
                maxNodeCount = max(maxNodeCount, nodeCount)
                return nodeCount
            
            # Pick 2 top paths
            singlePaths.sort()
            top1, top2 = singlePaths[-1], singlePaths[-2]
            
            # Path of top1 -> node -> top2
            doublePath = top1 + top2 + 1
            maxNodeCount = max(maxNodeCount, doublePath)
            return top1 + 1
        
        start = edges[0][0]
        postorder(start, start)
        
        return maxNodeCount - 1
