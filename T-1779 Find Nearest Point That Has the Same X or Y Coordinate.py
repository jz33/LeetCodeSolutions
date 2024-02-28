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
DoorDash interview:

题目就是给两个城市的list，一个是所有城市c[c1,c2,c3,c4]，x[4,7,9], y[1,2,3]
一个是需要query求距离的城市q[c3,c4]，求q里面每个城市到x或者y坐标重合（指 x相等或者y相等）的城市到最短距离

解法就是用map记录 {x1 : [c1, c2, c3]}  c1,c2,c3都有相同x1，sorted by y value in the list,
在query 一个城市q(qx, qy)‍‍‌‌‍‌‌‍‍‌‌‌‍‍‌‍‍的时候，求qx在map对应的list里面离qy最近的距离，用二分法求

面试的时候想到了二分法，但是面试官说时间来不及就不用写二分法，直接遍历map找就行，然后就挂了。。。
https://www.1point3acres.com/bbs/thread-1045459-1-1.html
'''