'''
1353. Maximum Number of Events That Can Be Attended
https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

You are given an array of events where events[i] = [startDayi, endDayi].
Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei.
You can only attend one event at any time d.

Return the maximum number of events you can attend.

Example 1:

Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.

Example 2:

Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4

Constraints:
    1 <= events.length <= 105
    events[i].length == 2
    1 <= startDayi <= endDayi <= 105
'''
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort() # sort by start then end
        heap = [] # min heap, [end, start], used to compare events with same start time
        nextStartDay = 0
        result = 0
        ei = 0 # iterator on events
        while ei < len(events) or heap:
            # If not heap, set next start day for next event
            if not heap:
                nextStartDay = events[ei][0]
            # Push all events with same start day into heap
            while ei < len(events) and events[ei][0] == nextStartDay:
                start, end = events[ei]
                heappush(heap, (end, start))
                ei += 1

            # Get result.
            end, _ = heappop(heap)
            # Some events are ended before next start day, cannot attend
            if end >= nextStartDay:
                # Current day is used, move to next day
                nextStartDay += 1
                result += 1
        return result



