'''
1192. Critical Connections in a Network
https://leetcode.com/problems/critical-connections-in-a-network/

There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections
forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi.
Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed,
will make some servers unable to reach some other server.

Return all critical connections in the network in any order.

Example 1:

Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.

Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]

Constraints:
    2 <= n <= 105
    n - 1 <= connections.length <= 105
    0 <= ai, bi <= n - 1
    ai != bi
    There are no repeated connections.
'''
class Solution:
    '''
    Tarjan, O(E+V)
    https://stackoverflow.com/questions/28917290/how-can-i-find-bridges-in-an-undirected-graph
    This is to find critical edges (bridges)
    '''
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # Build graph
        graph = [[] for _ in range(n)]
        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        # The DFS depth from origin. Set once and will not be changed.
        depths = [None] * n

        # The lowest dfs depth on a node. It is at least the depth,
        # and will be updated from neighbor's lowest depth
        lowestDepths = [None] * n

        # Critical edges
        bridges = []

        def dfs(curr: int, parent: int, depth: int):
            nonlocal depths, lowestDepths, bridges
            '''
            @curr: current node index
            @parent: parent node index
            @depth: current dfs depth
            '''
            depths[curr] = depth
            lowestDepths[curr] = depth

            for neighbor in graph[curr]:
                if depths[neighbor] is None:
                    
                    # If neighbor is yet visited, go for it
                    dfs(neighbor, curr, depth+1)
                    lowestDepths[curr] = min(lowestDepths[curr], lowestDepths[neighbor])

                    # So neighbor's depth is always + 1 of curr's depth.
                    # And if there is 2nd path from neighbor to curr, neighbor's
                    # lowest depth will be updated to curr's depth or even smaller.
                    # So by contraction, if neighbor's depth is same as its lowest,
                    # there is no 2nd path connecting neighbor to curr node.
                    if depths[neighbor] == lowestDepths[neighbor]:
                        bridges.append([curr, neighbor])
        
                elif neighbor != parent:
                    # Notice this update is different to above!
                    lowestDepths[curr] = min(lowestDepths[curr], depths[neighbor])

        dfs(0, 0, 0)
        return bridges
