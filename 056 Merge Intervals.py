'''
56. Merge Intervals
https://leetcode.com/problems/merge-intervals/
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n < 2:
            return intervals
        
        # Sort intervals by starting point
        intervals.sort(key = lambda x : x[0])
        
        res = []
        prev = intervals[0]
        for i in range(1, n):
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
