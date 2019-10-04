'''
133. Clone Graph
https://leetcode.com/problems/clone-graph/

Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.
Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.
 
Example:

Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

Explanation:
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.
Node 4's value is 4, and it has two neighbors: Node 1 and 3.
 
Note:
The number of nodes will be between 1 and 100.
The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as neighbor too.
You must return the copy of the given node as a reference to the cloned graph.
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
from typing import Dict

class Solution:
    def dfsRecursively(self, node: 'Node', book: Dict['Node','Node']) -> 'Node':
        if not node:
            return None
        
        if node not in book:
            newNode = Node(node.val, None)
            book[node] = newNode # mark as visited
            
            newNeighbors = []
            for neighbor in node.neighbors:
                newNeighbors.append(self.dfsRecursively(neighbor, book))

            newNode.neighbors = newNeighbors
            
        return book[node]
     
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Create a dict with {old node : new node},
        # which is also used to record whether node is copied
        book = {} 
        return self.dfsRecursively(node, book)
