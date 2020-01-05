'''
253. Meeting Rooms II
https://leetcode.com/problems/meeting-rooms-ii/

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
find the minimum number of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:

Input: [[7,10],[2,4]]
Output: 1
'''
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        points = []
        for s, e in intervals:
            points.append((s, 1))
            points.append((e, -1))          
        points.sort()
        
        maxOverlapped = 0
        overlapped = 0
        for p in points:
            overlapped += p[1]
            maxOverlapped = max(maxOverlapped, overlapped)
        
        return maxOverlapped
