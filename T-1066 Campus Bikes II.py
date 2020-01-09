'''
1066. Campus Bikes II
https://leetcode.com/problems/campus-bikes-ii/

On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M.
Each worker and bike is a 2D coordinate on this grid.

We assign one unique bike to each worker so that the sum of the Manhattan distances between
each worker and their assigned bike is minimized.

The Manhattan distance between two points p1 and p2 is Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|.

Return the minimum possible sum of Manhattan distances between each worker and their assigned bike.
'''
from heapq import heappush, heappop

class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        # Basically this question is to select a path from worker 0 to last worker,
        # find the path with smallest distance sum, classic Dijkstra.
        
        relations = [[None] * len(bikes) for _ in range(len(workers))]
        for wi, worker in enumerate(workers):
            for bi, bike in enumerate(bikes):
                relations[wi][bi] =  abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])
           
        # Since the size of bikes is <= 10, use a bitmap to record used bikes.
        # Notice the trick of this question, if using simple dijkstra, there will be many
        # Dijkstra with same workerId and same used bikes map!
        # Use set to filter out the duplicates
        heap = [(0, -1, 0)] # [(total distance, worker Id, used bikes)]
        computed = set() # set((workder Id, usedBikes))

        while heap:
            total, workerId, usedBikes = heappop(heap)

            if workerId == len(workers) - 1:
                return total

            if (workerId, usedBikes) in computed:
                continue

            computed.add((workerId, usedBikes))

            nextWorkerId = workerId + 1
            for bikerId in range(len(bikes)):
                if (usedBikes & (1 << bikerId)) == 0:
                    heappush(heap, (total + relations[nextWorkerId][bikerId], nextWorkerId, (usedBikes | (1 << bikerId))))

        return -1
