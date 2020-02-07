'''
847. Shortest Path Visiting All Nodes
https://leetcode.com/problems/patching-array/

An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is given as graph.

graph.length = N, and j != i is in the list graph[i] exactly once,
if and only if nodes i and j are connected.

Return the length of the shortest path that visits every node. You may start and stop at any node,
you may revisit nodes multiple times, and you may reuse edges.

Example 1:

Input: [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]

Example 2:

Input: [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]
 

Note:

1 <= graph.length <= 12
0 <= graph[i].length < graph.length
'''
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        N = len(graph)
        FULL = (1 << N) - 1 # all nodes visited bitmap
        
        computed = {} # {(visited node bitmap, current node) : step count}
        queue = []
        for i in range(N):
            state = (1 << i, i) # (visited node bitmap, current node)
            computed[state] = 0
            queue.append(state)
            
        while queue:
            newQueue = []
            for state in queue:
                steps = computed[state]
                bitmap, node = state
 
                for togo in graph[node]:
                    newBitmap = (bitmap | (1 << togo))
                    if newBitmap == FULL:
                        return steps + 1
                    
                    newState = (newBitmap, togo)
                    if newState not in computed or steps + 1 < computed[newState]:
                        computed[newState] = steps + 1
                        newQueue.append(newState)
            queue = newQueue
        
        return 0
