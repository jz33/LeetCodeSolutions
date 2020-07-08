'''
310. Minimum Height Trees
https://leetcode.com/problems/minimum-height-trees/

For an undirected graph with tree characteristics, we can choose any node as the root.
The result graph is then a rooted tree. Among all possible rooted trees,
those with minimum height are called minimum height trees (MHTs). Given such a graph,
write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1.
You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected,
[0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1 :

Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3 

Output: [1]

Example 2 :

Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5 

Output: [3, 4]
'''
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        '''
        The idea is to remove leaves layer by layer until
        there are no more inner nodes
        '''
        graph = collections.defaultdict(set)
        for x, y in edges:
            graph[x].add(y)
            graph[y].add(x)
                
        leaves = [i for i in range(n) if len(graph[i]) <= 1]
        innerNodeCount = n - len(leaves)
        
        while innerNodeCount > 0:
            newLeaves = []
            for leaf in leaves:
                # Remove this leaf
                parent = graph[leaf].pop()
                graph[parent].remove(leaf)
                
                # If parent becomes a new leaf
                if len(graph[parent]) == 1:
                    newLeaves.append(parent)
        
            leaves = newLeaves
            innerNodeCount -= len(newLeaves)

        return leaves
