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
    
    This is to find critical edges (bridges)
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
                lowestDepths[curr] = min(lowestDepths[curr], lowestDepths[neighbor])

                # So neighbor's depth is always + 1 of curr's depth.
                # And if there is 2nd path from neighbor to curr, neighbor's
                # lowest depth will be updated to curr's depth or even smaller.
                # So by contraction, if neighbor's depth is same as its lowest,
                # there is no 2nd path connecting neighbor to curr node.
                if depths[neighbor] == lowestDepths[neighbor]:
                    self.bridges.append([curr, neighbor])
       
            elif neighbor != parent:
                # Notice this update is different to above!
                lowestDepths[curr] = min(lowestDepths[curr], depths[neighbor])

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

        depths[curr] = lowestDepths[curr] = depth

        unvisitedNeighborCount = 0
        for neighbor in self.graph[curr]:
            if depths[neighbor] is None:
                unvisitedNeighborCount += 1

                # If neighbor is yet visited, go for it
                self.dfs(neighbor, curr, depth + 1)
                lowestDepths[curr] = min(lowestDepths[curr], lowestDepths[neighbor])

                # If curr is the staring node and has more than 1 unvisited neighbor (which means
                # at least 2 of curr's neighbors cannot visit each other in lower dfs cycles,
                # which means they can only reach each other via curr), then curr is articulation point.
                if curr == parent and unvisitedNeighborCount > 1: 
                    self.articulations.add(curr)
  
                # Or curr is not starting node but at least one of its neighbor's lowest depth
                # is bigger than curr's depth (which means there is no path from nodes previous
                # to curr that can reach this neighbor), then curr is also an articulation point
                if curr != parent and lowestDepths[neighbor] >= depths[curr]:
                    self.articulations.add(curr)

            elif neighbor != parent:
                lowestDepths[curr] = min(lowestDepths[curr], depths[neighbor])

    def criticalNodes(self, nodeCount: int, connections: List[List[int]]) -> List[int]:
        if nodeCount < 1:
            return []

        # Build graph
        graph = [[] for _ in range(nodeCount)]
        for edge in connections:
            a = edge[0]
            b = edge[1]
            graph[a].append(b)
            graph[b].append(a)

        # The DFS depth from origin. Set once and will not be changed.
        self.depths = [None] * nodeCount

        # The lowest dfs depth on a node. It is at least the depth,
        # and will be updated from neighbor's lowest depth
        self.lowestDepths = [None] * nodeCount

        self.graph = graph
        self.articulations = set() # result

        # Notice the graph may not be connected. Thus apply dfs to all nodes
        for i in range(nodeCount):
            if self.depths[i] is None:
                self.dfs(i, i, 0)

        return sorted(self.articulations)
