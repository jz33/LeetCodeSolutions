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
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        '''
        Safe nodes are not on cycle or its child nodes on cycle.
        '''
        nodeCount = len(graph)
 
        # The state of a node has following options:
        # 0. Undetermined (initial state)
        # 1. Visiting or cycled
        # 2. Non-cycled (safe)
        states = [0] * nodeCount
        
        def dfs(node: int):
            if states[node] != 0:
                # This is necessary because dfs starts on all nodes,
                # and so there can be duplicate visit on a node.
                return
            states[node] = 1

            cycled = True
            if len(graph[node]) == 0:
                cycled = False
            else:
                for togo in graph[node]:
                    dfs(togo)
                    
                    if states[togo] == 1:
                        cycled = True
                        break
                    else:
                        cycled = False

            if not cycled:
                states[node] = 2
        
        for i in range(nodeCount):
            dfs(i)

        return [i for i in range(nodeCount) if states[i] == 2]
