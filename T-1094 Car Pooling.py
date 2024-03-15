'''
1094. Car Pooling
https://leetcode.com/problems/car-pooling/

There is a car with capacity empty seats.
The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where
trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has num Passenger
si passengers and the locations to pick them up and drop them off are fromi and toi respectively.
The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips,
or false otherwise.

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false

Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true

Constraints:
    1 <= trips.length <= 1000
    trips[i].length == 3
    1 <= numPassengersi <= 100
    0 <= fromi < toi <= 1000
    1 <= capacity <= 105
'''
class Solution:
    '''
    Like intervals, similar to 253. Meeting Rooms II
    '''
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        points = [] # [(location, +- passengers)]
        for count, start, end in trips:
            points.append((start, count))
            points.append((end, -count))
        
        # Sort by location, then by passengers
        # End locations go first
        points.sort()
        
        accu = 0
        for _, count in points:
            accu += count
            if accu > capacity:
                return False
        return True
