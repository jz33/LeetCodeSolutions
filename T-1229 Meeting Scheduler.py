'''
1229. Meeting Scheduler
https://leetcode.com/problems/meeting-scheduler/

Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration,
return the earliest time slot that works for both of them and is of duration duration.

If there is no common time slot that satisfies the requirements, return an empty array.

The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.  

It is guaranteed that no two availability slots of the same person intersect with each other.
That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

Example 1:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
Output: [60,68]

Example 2:

Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
Output: []

Constraints:

1 <= slots1.length, slots2.length <= 10^4
slots1[i].length, slots2[i].length == 2
slots1[i][0] < slots1[i][1]
slots2[i][0] < slots2[i][1]
0 <= slots1[i][j], slots2[i][j] <= 10^9
1 <= duration <= 10^6 
'''
class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        x, y = 0, 0 # iterators
        slots1.sort()
        slots2.sort()
        while x < len(slots1) and y < len(slots2):
            s1 = slots1[x]
            s2 = slots2[y]
            if min(s1[1], s2[1]) - max(s1[0], s2[0]) >= duration:
                start = max(s1[0], s2[0])
                return [start , start + duration]
            
            if s1[1] < s2[1]:
                x += 1
            elif s1[1] > s2[1]:
                y += 1
            else:
                x += 1
                y += 1
        return []
