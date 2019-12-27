'''
849. Maximize Distance to Closest Person
https://leetcode.com/problems/maximize-distance-to-closest-person/

In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty. 

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him is maximized. 

Return that maximum distance to closest person.

Example 1:

Input: [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (seats[2]), then the closest person has distance 2.
If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.

Example 2:

Input: [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat, the closest person is 3 seats away.
This is the maximum distance possible, so the answer is 3.
Note:

1 <= seats.length <= 20000
seats contains only 0s or 1s, at least one 0, and at least one 1.
'''
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prevSeat = None
        maxDist = 0
        for i, e in enumerate(seats):
            if e == 1:
                if prevSeat is None:
                    # Sit 1st seat
                    maxDist = max(maxDist, i)
                else:
                    # Sit in the middle of 2 seats
                    maxDist = max(maxDist, (i - prevSeat) // 2)                    
                prevSeat = i
        
        # Sit last seat
        maxDist = max(maxDist, len(seats) - 1 - prevSeat)
        return maxDist        
