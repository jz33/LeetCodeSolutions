'''
785. Is Graph Bipartite?
https://leetcode.com/problems/is-graph-bipartite/

Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent subsets A and B such that
every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.
Each node is an integer between 0 and graph.length - 1.
There are no self edges or parallel edges: graph[i] does not contain i, and it doesn't contain any element twice.

Example 1:

Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true
Explanation: 
The graph looks like this:
0----1
|    |
|    |
3----2
We can divide the vertices into two groups: {0, 2} and {1, 3}.

Example 2:

Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation: 
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.
 
Note:

graph will have length in range [1, 100].
graph[i] will contain integers in range [0, graph.length - 1].
graph[i] will not contain i or duplicate values.
The graph is undirected: if any element j is in graph[i], then i will be in graph[j].
'''
from collections import deque

class Solution:
    def mark(self, origin: int, graph: List[List[int]], colors: List[int]) -> bool:
        '''
        BFS mark graph in 2 colors
        '''
        colors[origin] = 0

        queue = deque()
        queue.append(origin)

        while queue:
            node = queue.popleft()
            nodeColor = colors[node]

            for neighbor in graph[node]:
                if colors[neighbor] is None:
                    # Mark opposite color
                    colors[neighbor] = 1 - nodeColor
                    queue.append(neighbor)
                    
                elif nodeColor + colors[neighbor] != 1:
                    # The 2 colors are not opposite, return false
                    return False

        return True
    
    def isBipartite(self, graph: List[List[int]]) -> bool:
        '''
        The idea is to mark vertices with 2 colors.
        If 2 vertices on same edge are in same color,
        then the graph is not Bipartite
        '''
        size = len(graph)
        if not size:
            return True

        # Recorder of colors. There will be 2 colors, 0 & 1
        colors = [None] * size 
        
        # Notice the graph is not necessarily connected
        for i, c in enumerate(colors):
            if c is None:
                if not self.mark(i, graph, colors):
                    return False

        return True
