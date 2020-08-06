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
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        # Build a reversed stop -> bus graph
        stopToBus = collections.defaultdict(list) # {stop id : [bus ids]}
        for bus, stops in enumerate(routes):
            for stop in stops:
                stopToBus[stop].append(bus)
                
        visitedBuses = set()
        visitedStops = { S }
        stops = [S]
        busCount = 0
        while stops:
            newStops = []
            for stop in stops:
                if stop == T:
                    return busCount
                
                for bus in stopToBus[stop]:
                    if bus not in visitedBuses:
                        visitedBuses.add(bus)
                        for stop in routes[bus]:
                            if stop not in visitedStops:
                                visitedStops.add(stop)
                                newStops.append(stop)
            
            stops = newStops
            busCount += 1
        
        return -1   
