'''
1779. Find Nearest Point That Has the Same X or Y Coordinate
https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

You are given two integers, x and y, which represent your current location on a Cartesian grid: (x, y).
You are also given an array points where each points[i] = [ai, bi] represents that a point exists at (ai, bi).
A point is valid if it shares the same x-coordinate or the same y-coordinate as your location.

Return the index (0-indexed) of the valid point with the smallest Manhattan distance from your current location.
If there are multiple, return the valid point with the smallest index. If there are no valid points, return -1.

The Manhattan distance between two points (x1, y1) and (x2, y2) is abs(x1 - x2) + abs(y1 - y2).

Example 1:

Input: x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
Output: 2
Explanation: Of all the points, only [3,1], [2,4] and [4,4] are valid. Of the valid points, [2,4] and [4,4] have the smallest Manhattan distance from your current location, with a distance of 1. [2,4] has the smallest index, so return 2.

Example 2:

Input: x = 3, y = 4, points = [[3,4]]
Output: 0
Explanation: The answer is allowed to be on the same location as your current location.

Example 3:

Input: x = 3, y = 4, points = [[2,3]]
Output: -1
Explanation: There are no valid points.

Constraints:
    1 <= points.length <= 104
    points[i].length == 2
    1 <= x, y, ai, bi <= 104
'''
from typing import List, Tuple, Optional
from collections import defaultdict
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        smallestDist = float('inf')
        result = -1
        for i, p in enumerate(points):
            if p[0] == x or p[1] == y:
                dist = abs(p[0] - x) + abs(p[1] - y)
                if dist < smallestDist:
                    smallestDist = dist
                    result = i
        return result
    
'''
Real DoorDash interview:
https://leetcode.com/discuss/interview-question/1379696/DoorDASH-Onsite

A number of cities are arranged on a graph that has been divided up like an ordinary Cartesian plane.
Each city is located at an integral (x, y) coordinate intersection.
City names and locations are given in the form of three arrays: c, x, and y,
which are aligned by the index to provide the city name (c[i]),
and its coordinates, (x[i], y[i]).

Determine the name of the nearest city that shares either an x or a y coordinate with the queried city.
If no other cities share an x or y coordinate, return 'NONE'.
If two cities have the same distance to the queried city, q[i],
consider the one with an alphabetically shorter name (i.e. 'ab' < 'aba' < 'abb') as the closest choice.
The distance is the Manhattan distance, the absolute difference in x plus the absolute difference in y.
'''
def nearestCities(cities: List[str], xValues: List[int], yValues: List[int], queries: List[str]) -> List[str]:
    citySize = len(cities)
    cityToLocation = {} # {city name : (x, y)}
    xToCity = defaultdict(list) # {x value : [(y value, city name)]}
    yToCity = defaultdict(list) # {y value : [(x value, city name)]}
    for i in range(citySize):
        c = cities[i]
        x = xValues[i]
        y = yValues[i]
        cityToLocation[c] = (x, y)
        xToCity[x].append((y,c))
        yToCity[y].append((x,c))

    # Sort cities in each x, y
    for x, cs in xToCity.items():
        xToCity[x] = sorted(cs)
    for y, cs in yToCity.items():
        yToCity[y] = sorted(cs)

    # Answer query
    result = [None] * len(queries)
    for ri, city in enumerate(queries):
        location = cityToLocation.get(city)
        if location is not None:
            x, y = location
            xCity = cityFind(xToCity[x], y)
            yCity = cityFind(yToCity[y], x)
            result[ri] = cityCompare(xCity, yCity)
    return result

def cityFind(cities: List[Tuple[int, str]], target: int) -> Optional[str]:
    # Binary search to find target value in cities array
    left = 0
    right = len(cities) - 1
    mid = left
    while left <= right:
        mid = left + (right - left) // 2
        midVal, _ = cities[mid]
        if midVal == target:
            break
        if midVal < target:
            left = mid + 1
        else:
            right = mid - 1
    # Now cities[mid] is the target, then find its left or right
    cityLeft = cities[mid-1][1] if mid - 1 >= 0 else None
    cityRight = cities[mid+1][1] if mid + 1 < len(cities) else None
    return cityCompare(cityLeft, cityRight)

def cityCompare(cityLeft: Optional[str], cityRight: Optional[str]) -> Optional[str]:
    if not cityLeft and not cityRight:
        return None
    if not cityLeft:
        return cityRight
    if not cityRight:
        return cityLeft
    return cityLeft if cityLeft < cityRight else cityRight

cities = ['Bellevue', 'London', 'Miami', 'Paris', 'Seattle']
xValues = [5, 6, 7, 5, 10]
yValues = [12, 9, 8, 7, 12]
queries = ['Bellevue', 'Seattle']
print(nearestCities(cities, xValues, yValues, queries))