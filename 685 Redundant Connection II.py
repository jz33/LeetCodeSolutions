'''
685. Redundant Connection II
Hard

In this problem, a rooted tree is a directed graph such that,
there is exactly one node (the root) for which all other nodes are descendants of this node,
plus every node has exactly one parent, except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N),
with one additional directed edge added. The added edge has two different vertices chosen from 1 to N,
and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges.
Each element of edges is a pair [u, v] that represents a directed edge connecting nodes u and v,
where u is a parent of child v.

Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes.
If there are multiple answers, return the answer that occurs last in the given 2D-array.

Example 1:

Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given directed graph will be like this:
  1
 / \
v   v
2-->3

Example 2:

Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
Output: [4,1]
Explanation: The given directed graph will be like this:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3

'''
class UnionFind:
    def __init__(self, nodeCount: int):
        # The Union-Find graph, where
        # node[i] points to the parent (not necessisarily its root) of node i+1
        # nodes[0] is unused
        self.nodes = [None] * (nodeCount + 1)
    
    def GetRoot(self, nodeId: int) -> int:
        nodes = self.nodes        
        while nodes[nodeId]:
            nodeId = nodes[nodeId]
        return nodeId
    
    def Union(self, childNode: int, parentNode: int) -> bool:
        cr = self.GetRoot(childNode)
        pr = self.GetRoot(parentNode)
        
        if cr == pr:
            return False
        
        self.nodes[cr] = pr
        return True
    
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        redundant = None
        graph = UnionFind(len(edges))
        for edge in edges:
            if not graph.Union(edge[0], edge[1]):
                redundant = edge               
        return redundant
    
    def isValidTree(self, edges: List[List[int]], removedEdge: List[int]) -> bool:
        graph = UnionFind(len(edges))
        for edge in edges:
            if edge == removedEdge:
                continue
            if not graph.Union(edge[0], edge[1]):
                return False             
        return True
    
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        2 cases the graph is not a valid tree:
        1. A Cycle
        2. A node has 2 parents
        '''
        # Find if there is a node has 2 parents
        N = len(edges)
        nodes = [None] * (N+1)
        candidateEdges = []
        for edge in edges:
            parent = edge[0]
            child = edge[1]
            if nodes[child] is None:
                nodes[child] = parent
            else:
                candidateEdges += [edge, [nodes[child], child]]
                break
        
        if not candidateEdges:
            # If no node has 2 parents, there must be a cycle
            # Use solution 684 from Redundant Connection
            return self.findRedundantConnection(edges)
        else:
            # Otherwise, remove 1 candidate, see if valid
            # Notice candidateEdges[0] appears later
            if self.isValidTree(edges, candidateEdges[0]):
                return candidateEdges[0]
            else:
                return candidateEdges[1]
