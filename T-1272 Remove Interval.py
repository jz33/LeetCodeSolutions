'''
1272. Remove Interval
https://leetcode.com/problems/remove-interval/

Given a sorted list of disjoint intervals, each interval intervals[i] = [a, b] represents
the set of real numbers x such that a <= x < b.

We remove the intersections between any interval in intervals and the interval toBeRemoved.

Return a sorted list of intervals after all such removals.

Example 1:

Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
Output: [[0,1],[6,7]]

Example 2:

Input: intervals = [[0,5]], toBeRemoved = [2,3]
Output: [[0,2],[3,5]]
 

Constraints:

1 <= intervals.length <= 10^4
-10^9 <= intervals[i][0] < intervals[i][1] <= 10^9
'''
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        res = []
        for s, e in intervals:
            if e < toBeRemoved[0] or toBeRemoved[1] < s:
                # No intersection with toBeRemoved
                res.append([s, e])
            else:
                # Has intersections
                if s < toBeRemoved[0]:
                    res.append([s, toBeRemoved[0]])
                if toBeRemoved[1] < e :
                    res.append([toBeRemoved[1], e])                 
        return res
