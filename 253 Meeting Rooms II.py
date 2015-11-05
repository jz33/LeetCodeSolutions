from heapq import heappush, heappop
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        length = len(intervals)
        if length < 2: return length
        intervals.sort(key = lambda tup : tup.start)
        
        # A min-heap to hold current meeting end times
        h = []
        heappush(h,intervals[0].end)
        maxRoom = 1
        for i in xrange(1,length):
            iv = intervals[i]
            while len(h) > 0 and iv.start >= h[0]:
                heappop(h)
            heappush(h,iv.end)
            maxRoom = max(maxRoom,len(h))
        return maxRoom
