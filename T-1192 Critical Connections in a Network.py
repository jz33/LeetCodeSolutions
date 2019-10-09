'''
1192. Critical Connections in a Network
https://leetcode.com/problems/critical-connections-in-a-network/

There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where
connections[i] = [a, b] represents a connection between servers a and b.
Any server can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.

Example 1:

Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
'''
class Solution:
    '''
    Tarjan, O(E+V)
    https://stackoverflow.com/questions/28917290/how-can-i-find-bridges-in-an-undirected-graph
    '''
    def dfs(self, curr: int, parent: int, depth: int):
        '''
        @curr: current node index
        @parent: parent node index
        @depth: current dfs depth
        '''
        depths = self.depths
        lowestDepths = self.lowestDepths

        depths[curr] = depth
        lowestDepths[curr] = depth

        for neighbor in self.graph[curr]:
            if depths[neighbor] is None:
                # If neighbor is yet visited, go for it
                self.dfs(neighbor, curr, depth+1)
          
                # So neighbor's depth is always +1 of curr's depth.
                # And if there is 2nd path from neighbor to curr, neighbor's
                # lowest depth will be updated to curr's lowest depth or smaller.
                # So by contraction, if neighbor's depth is same as its lowest,
                # there is no 2nd path connection neighbor to curr
                if depths[neighbor] == lowestDepths[neighbor]:
                    self.bridges.append([curr, neighbor])

                lowestDepths[curr] = min(lowestDepths[curr], lowestDepths[neighbor])

            elif neighbor != parent:
                lowestDepths[curr] = min(lowestDepths[curr], lowestDepths[neighbor])

    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        if n < 1:
            return []

        # Build graph
        graph = [[] for _ in range(n)]
        for edge in connections:
            a = edge[0]
            b = edge[1]
            graph[a].append(b)
            graph[b].append(a)

        # The DFS depth from origin. Set once and will not be changed.
        self.depths = [None] * n

        # The lowest dfs depth on a node. It is at least the depth,
        # and will be updated from neighbor's lowest depth
        self.lowestDepths = [None] * n

        self.graph = graph
        self.bridges = []
        self.dfs(0, 0, 0)
        return self.bridges
