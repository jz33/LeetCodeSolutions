'''
252. Meeting Rooms
https://leetcode.com/problems/meeting-rooms/

Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
determine if a person could attend all meetings.

Example 1:

Input: [[0,30],[5,10],[15,20]]
Output: false

Example 2:

Input: [[7,10],[2,4]]
Output: true
'''
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        for i, m in enumerate(intervals):
            if i > 0 and m[0] < intervals[i-1][1]:
                return False
        return True
