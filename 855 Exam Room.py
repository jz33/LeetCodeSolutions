'''
855. Exam Room
https://leetcode.com/problems/exam-room/

There is an exam room with n seats in a single row labeled from 0 to n - 1.

When a student enters the room, they must sit in the seat that maximizes the distance tothe closest person.
If there are multiple such seats, they sit in the seat with the lowest number. =
If no one is in the room, then the student sits at seat number 0.

Design a class that simulates the mentioned exam room.

Implement the ExamRoom class:

    ExamRoom(int n) Initializes the object of the exam room with the number of the seats n.
    
    int seat() Returns the label of the seat at which the next student will set.
    
    void leave(int p) Indicates that the student sitting at seat p will leave the room.
    It is guaranteed that there will be a student sitting at seat p.

Example 1:

Input
["ExamRoom", "seat", "seat", "seat", "seat", "leave", "seat"]
[[10], [], [], [], [], [4], []]
Output
[null, 0, 9, 4, 2, null, 5]

Explanation
ExamRoom examRoom = new ExamRoom(10);
examRoom.seat(); // return 0, no one is in the room, then the student sits at seat number 0.
examRoom.seat(); // return 9, the student sits at the last seat number 9.
examRoom.seat(); // return 4, the student sits at the last seat number 4.
examRoom.seat(); // return 2, the student sits at the last seat number 2.
examRoom.leave(4);
examRoom.seat(); // return 5, the student sits at the last seat number 5.

Constraints:
    1 <= n <= 109
    It is guaranteed that there is a student sitting at seat p.
    At most 104 calls will be made to seat and leave.
'''
from sortedcontainers import SortedList

class Interval:
    def __init__(self, maxSize, left, right):
        """
        @maxSize: maximum size of the interval (always n in this question)
        @left: left bound, inclusive
        @right: right bound, inclusive
        left <= right
        """
        self.maxSize = maxSize
        self.left = left
        self.right = right
        self.size = right - left + 1

    def getSeatId(self) -> int:
        """
        Get the idea seat id
        """
        if self.left == 0:
            return 0
        if self.right == self.maxSize - 1:
            return self.maxSize - 1
        return (self.left + self.right) // 2

    def getDistance(self) -> int:
        """
        Get the nearest distance to bounds if set a seat.
        Used for __lt__
        """
        if self.left == 0:
            return self.right + 1
        if self.right == 0:
            return self.maxSize - self.left
        return self.getSeatId() - self.left + 1

    def __lt__(self, that) -> bool:
        """
        Used for sorted list comparison
        """
        selfDistance = self.getDistance()
        thatDistance = that.getDistance()
        if selfDistance != thatDistance:
            return selfDistance < thatDistance
        # Prefer earlier indexed interval to back
        return self.left > that.left

    def __repr__(self) -> str:
        """
        Used for debugging
        """
        return f"[{self.left}, {self.right}]"

    def __eq__(self, that) -> bool:
        """
        Used for removal
        """
        return (
            self.left == that.left
            and self.right == that.right
            and self.maxSize == that.maxSize
        )

class ExamRoom:
    def __init__(self, n: int):
        self.n = n
        self.seats = SortedList()
        self.intervals = SortedList([Interval(n, 0, n - 1)])

    def tryAddInterval(self, left, right) -> None:
        if left <= right:
            self.intervals.add(Interval(self.n, left, right))

    def seat(self) -> int:
        # Pop the last interval, which should be the largest sized
        largest = self.intervals.pop()
        seatId = largest.getSeatId()
        # Possibly add 2 intervals
        self.tryAddInterval(largest.left, seatId - 1)
        self.tryAddInterval(seatId + 1, largest.right)
        # Save seat
        self.seats.add(seatId)
        return seatId

    def tryRemoveInterval(self, left, right) -> None:
        if left <= right:
            self.intervals.discard(Interval(self.n, left, right))

    def leave(self, seatId: int) -> None:
        # Try find left interval of seatId
        leftSeatId = next(
            self.seats.irange(maximum=seatId, inclusive=(True, False), reverse=True),
            -1,
        )
        # Try find right interval of seatId
        rightSeatId = next(
            self.seats.irange(minimum=seatId, inclusive=(False, True)),
            self.n,
        )
        # Remove seat
        self.seats.discard(seatId)
        # Remove intervals
        self.tryRemoveInterval(leftSeatId + 1, seatId - 1)
        self.tryRemoveInterval(seatId + 1, rightSeatId - 1)
        # Add the merged interval
        self.intervals.add(Interval(self.n, leftSeatId + 1, rightSeatId - 1))
