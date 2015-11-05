# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals.sort(key = lambda tup : tup.start)
        for i,v in enumerate(intervals):
            if i > 0 and v.start < intervals[i-1].end:
                return False
        return True
