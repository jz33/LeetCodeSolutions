'''
547. Friend Circles
https://leetcode.com/problems/friend-circles/
'''
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        '''
        A classic Union-Find implementation
        '''
        count = len(M)
        if count == 0:
            return 0
    
        # The node : root graph.
        # '-1' means no root is set yet, aka itself is root
        graph = [-1] * count
    
        def getRoot(i):
            # Not if graph[i] != -1
            while graph[i] != -1:
                i = graph[i]
            return i
              
        # Find all "edges", avoid duplicated matrix iteration
        for i in range(count):
            for j in range(i + 1, count):
                if M[i][j] == 1:
                    ri = getRoot(i)
                    rj = getRoot(j)
                    
                    # Point bigger indexed node to smaller indexed node
                    if ri != rj:
                        if ri < rj:
                            graph[rj] = ri
                        else:
                            graph[ri] = rj
        
        # Count all roots
        return sum(1 for node in graph if node == -1)
