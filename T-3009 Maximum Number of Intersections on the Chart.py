'''
3009. Maximum Number of Intersections on the Chart
https://leetcode.com/problems/maximum-number-of-intersections-on-the-chart/

There is a line chart consisting of n points connected by line segments.
You are given a 1-indexed integer array y.
The kth point has coordinates (k, y[k]).
There are no horizontal lines; that is, no two consecutive points have the same y-coordinate.

We can draw an infinitely long horizontal line.
Return the maximum number of points of intersection of the line with the chart.

Example 1:

Input: y = [1,2,1,2,1,3,2]
Output: 5
Explanation: As you can see in the image above, the line y = 1.5 has 5 intersections with the chart (in red crosses).
You can also see the line y = 2 which intersects the chart in 4 points (in red crosses).
It can be shown that there is no horizontal line intersecting the chart at more than 5 points.
So the answer would be 5.

Example 2:

Input: y = [2,1,3,4,5]
Output: 2
Explanation: As you can see in the image above, the line y = 1.5 has 2 intersections with the chart (in red crosses).
You can also see the line y = 2 which intersects the chart in 2 points (in red crosses).
It can be shown that there is no horizontal line intersecting the chart at more than 2 points.
So the answer would be 2.

Constraints:
    2 <= y.length <= 105
    1 <= y[i] <= 109
    y[i] != y[i + 1] for i in range [1, n - 1]
'''
class Solution:
    def maxIntersectionCount(self, ys: List[int]) -> int:
        '''
        Similar to 253. Meeting Rooms II, needs to pre-process into intervals.
        https://leetcode.com/problems/maximum-number-of-intersections-on-the-chart/solutions/4611370/meeting-rooms-with-additional-interval-processing/
        '''
        intervals = Counter() # { start / end : -1 / +1 }
        
        def appendInterval(start: int, end: int):
            nonlocal intervals
            intervals[start] += 1
            intervals[end] -= 1

        first = [min(ys[0], ys[1]), max(ys[0], ys[1]) + 0.5]
        appendInterval(first[0], first[1])

        for i in range(1, len(ys)-1):
            start = ys[i]
            end = ys[i+1]
            if start < end:
                # add 0.5 to either kind interval, to avoid calculate a point twice
                appendInterval(start+0.5, end+0.5)
            else:
                appendInterval(end, start)

        # Now its 253. Meeting Rooms II
        result = 0
        count = 0
        meetings = sorted(intervals.items())
        for _, v in meetings:
            count += v
            result = max(result, count)
        return result
