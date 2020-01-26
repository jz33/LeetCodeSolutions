'''
857. Minimum Cost to Hire K Workers
https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

There are N workers.  The i-th worker has a quality[i] and a minimum wage expectation wage[i].

Now we want to hire exactly K workers to form a paid group.
When hiring a group of K workers, we must pay them according to the following rules:

Every worker in the paid group should be paid in the ratio of their quality compared to other workers in the paid group.
Every worker in the paid group must be paid at least their minimum wage expectation.
Return the least amount of money needed to form a paid group satisfying the above conditions.

Example 1:

Input: quality = [10,20,5], wage = [70,50,30], K = 2
Output: 105.00000
Explanation: We pay 70 to 0-th worker and 35 to 2-th worker.

Example 2:

Input: quality = [3,1,10,10,1], wage = [4,8,2,2,7], K = 3
Output: 30.66667
Explanation: We pay 4 to 0-th worker, 13.33333 to 2-th and 3-th workers seperately. 
'''
from heapq import heappush, heappop

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], K: int) -> float:
        size = len(quality)
        
        # For each worker i, there is a ratio from minimum wage / quality.
        # And total cost will be ratio * total worker quality.
        # We put smaller ratio workers into a container, then
        # use ratio of latest pushed worker, so earlier worker's 
        # minimum wage requirement can meet. 
        # If the container is bigger than K, popup the worker with
        # largest quality
        ratios = sorted(zip((wage[i] / quality[i] for i in range(size)), range(size)))
        
        heap = [] # [quality], maximum heap
        totalQuality = 0
        totalCost = float('inf')
        for ratio, workerId in ratios:
            q = quality[workerId]
            heappush(heap, -q)
            totalQuality += q
            if len(heap) > K:
                totalQuality += heappop(heap)
            if len(heap) == K:
                totalCost = min(totalCost, totalQuality * ratio)
        return totalCost
