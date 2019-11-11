'''
815. Bus Routes
https://leetcode.com/problems/bus-routes/

We have a list of bus routes.
Each routes[i] is a bus route that the i-th bus repeats forever. For example if routes[0] = [1, 5, 7],
this means that the first bus (0-th indexed) travels in the sequence 1->5->7->1->5->7->1->... forever.

We start at bus stop S (initially not on a bus), and we want to go to bus stop T.
Travelling by buses only, what is the least number of buses we must take to reach our destination? Return -1
if it is not possible.

Example:

Input: 
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6

Output: 2

Explanation:
The best strategy is take the first bus to the bus stop 7, then take the second bus to the bus stop 6.
'''
from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        # {stop id : [bus ids]}
        graph = defaultdict(list)
        for i,stops in enumerate(routes):
            for s in stops:
                graph[s].append(i)
                
        visitedBuses = set()
        visitedStops = { S }
        queue = deque()
        queue.append(S)
        busCount = 0
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == T:
                    return busCount
                
                for bus in graph[node]:
                    if bus not in visitedBuses:
                        visitedBuses.add(bus)
                        for stop in routes[bus]:
                            if stop not in visitedStops:
                                visitedStops.add(stop)
                                queue.append(stop)
                         
            busCount += 1
        
        return -1            
