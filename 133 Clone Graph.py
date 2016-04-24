'''
Clone Graph
https://leetcode.com/problems/clone-graph/
'''
# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def recursive(self,src,mapper):
        if src is None: return None
        if src not in mapper:
            cpy = UndirectedGraphNode(src.label)
            mapper[src] = cpy
            for n in src.neighbors:
                cpy.neighbors.append(self.recursive(n,mapper))
        return mapper[src]
    
    def cloneGraph(self, src):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        mapper = {}
        return self.recursive(src,mapper)
