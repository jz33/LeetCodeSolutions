'''
218. The Skyline Problem
https://leetcode.com/problems/the-skyline-problem/

A city's skyline is the outer contour of the silhouette formed by all the buildings
in that city when viewed from a distance.
Given the locations and heights of all the buildings,
return the skyline formed by these buildings collectively.

The geometric information of each building is given in the array buildings where
buildings[i] = [lefti, righti, heighti]:

    lefti is the x coordinate of the left edge of the ith building.
    righti is the x coordinate of the right edge of the ith building.
    heighti is the height of the ith building.

You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.

The skyline should be represented as a list of "key points" sorted by
their x-coordinate in the form [[x1,y1],[x2,y2],...].
Each key point is the left endpoint of some horizontal segment in the skyline except
the last point in the list, which always has a y-coordinate 0 and is used to mark
the skyline's termination where the rightmost building ends.
Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.

Note: There must be no consecutive horizontal lines of equal height in the output skyline.
For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable;
the three lines of height 5 should be merged into one in the final output as such:
[...,[2 3],[4 5],[12 7],...]

Example 1:

Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings.
The red points in figure B represent the key points in the output list.

Example 2:

Input: buildings = [[0,2,3],[2,5,3]]
Output: [[0,3],[5,0]]

Constraints:
    1 <= buildings.length <= 104
    0 <= lefti < righti <= 231 - 1
    1 <= heighti <= 231 - 1
    buildings is sorted by lefti in non-decreasing order.
'''
from heapq import heappush, heappop

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        size = len(buildings)      
        heap = [] # [(-height, x-axis index)], a max heap for height
        skyline = [] # [[x-axis index, height]]

        bi = 0 # iterator on buildings
        while bi < size or heap:
            x = 0 # The x-axis index for skyline

            # If this building is overlapped to previous building:
            if not heap or bi < size and buildings[bi][0] <= heap[0][1]:
                x = buildings[bi][0]

                # Push in all buildings with same left bound
                while bi < size and buildings[bi][0] == x:
                    # Push the height and right bound
                    heappush(heap, (-buildings[bi][2], buildings[bi][1]))
                    bi += 1
        
            # Else, not overlapped
            else:
                x = heap[0][1]

                # Pop all elements with right bound smaller or equal to x
                # because they are no longer needed
                while heap and heap[0][1] <= x:
                    heappop(heap)

            # The height of the skyline is the maximum height in the heap
            height = 0 if not heap else -heap[0][0]

            # Do not add duplicate height
            if len(skyline) == 0 or height != skyline[-1][1]:
                skyline.append([x, height])

        return skyline

# Test cases
[[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
[[2,9,10],[9,12,15]]
[[1,2,1],[1,2,2],[1,2,3]]
[[2,4,70],[3,8,30],[6,100,41],[7,15,70],[10,30,102],[15,25,76],[60,80,91],[70,90,72],[85,120,59]]
