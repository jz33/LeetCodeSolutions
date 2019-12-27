'''
802. Find Eventual Safe States
https://leetcode.com/problems/find-eventual-safe-states/

In a directed graph, we start at some node and every turn, walk along a directed edge of the graph.
If we reach a node that is terminal (that is, it has no outgoing directed edges), we stop.

Now, say our starting node is eventually safe if and only if we must eventually walk to a terminal node.
More specifically, there exists a natural number K so that for any choice of where to walk,
we must have stopped at a terminal node in less than K steps.

Which nodes are eventually safe?  Return them as an array in sorted order.

The directed graph has N nodes with labels 0, 1, ..., N-1, where N is the length of graph.
The graph is given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge of the graph.

Example:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]
Here is a diagram of the above graph.

Illustration of graph

Note:

graph will have length at most 10000.
The number of edges in the graph will not exceed 32000.
Each graph[i] will be a sorted list of different integers, chosen within the range [0, graph.length - 1].
'''
class Solution:
    def dfs(self, node):
        if self.results[node] != 0:
            return
        self.results[node] = 1 # visiting
        
        cycled = False
        for neighbor in self.graph[node]:
            if self.results[neighbor] == 1 or self.results[neighbor] == 2:
                cycled = True
            else:
                self.dfs(neighbor)
                if self.results[neighbor] == 2:
                    cycled = True    

        self.results[node] = 2 if cycled else 3  
                            
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        '''
        Detect cylces on directed graph.
        If a node is on cycle or any of its sub nodes on cycle, it is not safe start.
        '''
        self.graph = graph

        # Result records
        # 0: undetermined
        # 1: visiting
        # 2: cycled
        # 3: uncycled
        self.results = [0] * len(graph)
        
        for i in range(len(graph)):
            self.dfs(i)
            
        return [i for i in range(len(graph)) if self.results[i] == 3]
