'''
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/

Given an array of intervals where intervals[i] = [starti, endi],
merge all overlapping intervals, and return an array of the non-overlapping intervals
that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
    1 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 104
'''
class Solution:
    '''
    Real TikTok interview question: 20240125
    '''
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        result = []
        prev = intervals[0]
        for i in range(1, len(intervals)):
            curr = intervals[i]
            if curr[0] > prev[1]:
                # If current interval's starting point is bigger than
                # previous's end point, they are not overlapped
                result.append(prev)
                prev = curr
            else:
                # Else, they are overlapped. To combine current and previous,
                # the starting point is previous's starting point,
                # the end point is max of these 2's end point
                prev[1] = max(prev[1], curr[1])
        result.append(prev)
        return result
