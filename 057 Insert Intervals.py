# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        res = []
        start = newInterval.start
        end = newInterval.end
        t = len(intervals)
        for i,v in enumerate(intervals):
            if start <= v.end:
                if end < v.start:
                    t = i
                    break
                start = min(start, v.start)
                end = max(end,v.end)
            else:
                res.append(v)
        res.append(Interval(start,end))
        res.extend(intervals[t:])
        return res
