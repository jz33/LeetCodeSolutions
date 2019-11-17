'''
1168. Optimize Water Distribution in a Village
https://leetcode.com/problems/optimize-water-distribution-in-a-village/

There are n houses in a village. We want to supply water for all the houses by building wells and laying pipes.

For each house i, we can either build a well inside it directly with cost wells[i],
or pipe in water from another well to it. The costs to lay pipes between houses are given by the array pipes,
where each pipes[i] = [house1, house2, cost] represents the cost to connect house1 and house2 together using a pipe.
Connections are bidirectional.

Find the minimum total cost to supply water to all houses.

Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
Output: 3
Explanation: 
The image shows the costs of connecting houses using pipes.
The best strategy is to build a well in the first house with cost 1 and connect the other houses to it with cost 2
so the total cost is 3.
'''
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        '''
        Kruskal
        '''
        # Build edges, [(cost, from, togo)]. Notice the node indexes
        edges = [(c, 0, i) for i, c in enumerate(wells, start=1)]
        edges += [(c, f, t) for f, t, c in pipes]
        edges.sort()
        
        # There are n+1 nodes. Nodes start from 0.
        nodes = list(range(n+1))      
        def find(i):
            if nodes[i] != i:
                nodes[i] = find(nodes[i])
            return nodes[i]
        
        totalCost = 0
        totalEdgeCount = 0
        for c, f, t in edges:
            rf = find(f)
            rt = find(t)
            if rf != rt:
                nodes[rf] = rt
                totalCost += c
                totalEdgeCount += 1
                if totalEdgeCount == n:
                    # Only n edges needed to connect n+1 nodes
                    return totalCost
                
        return -1
