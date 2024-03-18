'''
253. Meeting Rooms II
https://leetcode.com/problems/meeting-rooms-ii/

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi],
return the minimum number of conference rooms required.

Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1

Constraints:
    1 <= intervals.length <= 104
    0 <= starti < endi <= 106
'''
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        points = []
        for start, end in intervals:
            points.append((start, 1))
            points.append((end, -1))

        # The end will appear before start        
        points.sort()
        
        maxOverlapped = 0
        overlapped = 0
        for p in points:
            overlapped += p[1]
            maxOverlapped = max(maxOverlapped, overlapped)
        return maxOverlapped
