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
'''
Real interview question of Convoy, inc, 20200814
'''

from collections import defaultdict

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # Build a {stop : [bus ids]} map
        stopToBuses = defaultdict(list)
        for busId, stops in enumerate(routes):
            for stop in stops:
                stopToBuses[stop].append(busId)

        # Save the bus id to improve performance
        visitedBuses = set() # set(busIds)
        visitedStops = { source } # set(stopIds)
        stops = [source]
        steps = 0
        while stops:
            newStops = []
            for stop in stops:
                if stop == target:
                    return steps
                
                for busId in stopToBuses[stop]:
                    if busId not in visitedBuses:
                        visitedBuses.add(busId)
                        for stop in routes[busId]:
                            if stop not in visitedStops:
                                visitedStops.add(stop)
                                newStops.append(stop)
            stops = newStops
            steps += 1
        return -1
