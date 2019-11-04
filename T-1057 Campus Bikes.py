'''
1057. Campus Bikes
https://leetcode.com/problems/campus-bikes/

On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M.
Each worker and bike is a 2D coordinate on this grid.

Our goal is to assign a bike to each worker.
Among the available bikes and workers, we choose the (worker, bike) pair with the shortest Manhattan distance between
each other, and assign the bike to that worker.
(If there are multiple (worker, bike) pairs with the same shortest Manhattan distance,
we choose the pair with the smallest worker index; if there are multiple ways to do that,
we choose the pair with the smallest bike index). We repeat this process until there are no available workers.

The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

Return a vector ans of length N, where ans[i] is the index (0-indexed) of the bike that the i-th worker is assigned to.
'''
class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        relations = [None] * (len(workers) * len(bikes))
        ri = 0
        
        for wi, worker in enumerate(workers):
            for bi, bike in enumerate(bikes):
                distance = abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
                # Simply use python's tuple is faster than create a class
                relations[ri] = ((distance, wi, bi))
                ri += 1
        
        workerToBike = [None] * len(workers)
        usedBikes = [None] * len(bikes)
        for _, wi,bi in sorted(relations):
            if workerToBike[wi] is None and usedBikes[bi] is None:
                workerToBike[wi] = bi
                usedBikes[bi] = wi
                
        return workerToBike 
