'''
787. Cheapest Flights Within K Stops

There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst,
your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200

The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.

Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500

The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.

Note:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.
'''
from collections import defaultdict
from heapq import heappush, heappop

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        '''
        Dijkstra, worst time O(E + V * logV)
        '''
        graph = defaultdict(list)
        for flight in flights:
            f = flight[0] # from
            t = flight[1] # togo
            c = flight[2] # cost
            graph[f].append((t, c))

        heap = [(0, src, 0)] # [(cost, node, step)]

        # BFS. No need to record visisted nodes as there are no cycles
        while heap:
            cost, node, step = heappop(heap)
            if node == dst:
                return cost

            if step < K + 1:
                for t,c in graph[node]:
                    heappush(heap, (cost + c, t, step+1))

        return -1
