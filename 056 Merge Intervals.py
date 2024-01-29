'''
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''
class Solution:
    '''
    Real TikTok interview question: 20240125
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort()
        
        res = []
        prev = intervals[0]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] > prev[1]:
                # If current interval's starting point is bigger than
                # previous's end point, they are not overlapped
                res.append(prev)
                prev = curr
            else:
                # Else, they are overlapped. To combine current and previous,
                # the starting point is previous's starting point,
                # the end point is max of these 2's end point
                prev[1] = max(prev[1], curr[1])
        
        res.append(prev)
        return res
