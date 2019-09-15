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
from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        Essentially, this is to ask the most overlapped interval count
        '''
        # Sort meetings from start time
        intervals.sort(key = lambda x : x[0])
        
        roomCount = 0
        heap = [] # Heap of meeting end time
        
        for meeting in intervals:
            # If current meeting starts after previous meeting,
            # no need for new room
            while len(heap) > 0 and meeting[0] >= heap[0]:
                heappop(heap)
                
            heappush(heap, meeting[1])
            
            # The meetings in heap now all need there individual room,
            # because they are overlapped          
            roomCount = max(roomCount, len(heap))
            
        return roomCount
