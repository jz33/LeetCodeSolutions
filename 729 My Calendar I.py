'''
729. My Calendar I
https://leetcode.com/problems/my-calendar-i/

You are implementing a program to use as your calendar.
We can add a new event if adding the event will not cause a double booking.

A double booking happens when two events have some non-empty intersection
(i.e., some moment is common to both events.).

The event can be represented as a pair of integers start and end that
represents a booking on the half-open interval [start, end),
the range of real numbers x such that start <= x < end.

Implement the MyCalendar class:

    MyCalendar() Initializes the calendar object.
    
    boolean book(int start, int end) Returns true if the event can be added
    to the calendar successfully without causing a double booking.
    Otherwise, return false and do not add the event to the calendar.

Example 1:

Input
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
Output
[null, true, false, true]

Explanation
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False, It can not be booked because time 15 is already booked by another event.
myCalendar.book(20, 30); // return True, The event can be booked, as the first event takes every time less than 20, but not including 20.

Constraints:
    0 <= start < end <= 109
    At most 1000 calls will be made to book.
'''
from sortedcontainers import SortedDict

def isOverLapped(aLeft: int, aRight: int, bLeft: int, bRight: int) -> int:
    return min(aRight, bRight) > max(aLeft, bLeft)

class MyCalendar:
    def __init__(self):
        self.events = SortedDict()  # {start : end}

    def book(self, start: int, end: int) -> bool:
        nearestLeft = next(self.events.irange(maximum=start, reverse=True), None)
        if nearestLeft != None:
            nearestLeftEnd = self.events[nearestLeft]
            if isOverLapped(nearestLeft, nearestLeftEnd, start, end):
                return False

        nearestRight = next(self.events.irange(maximum=end, inclusive=(True, False), reverse=True), None)
        if nearestRight != None:
            nearestRightEnd = self.events[nearestRight]
            if isOverLapped(nearestRight, nearestRightEnd, start, end):
                return False

        self.events[start] = end
        return True
