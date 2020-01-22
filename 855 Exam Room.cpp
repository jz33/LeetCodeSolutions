/*
855. Exam Room
https://leetcode.com/problems/exam-room/

In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1.

When a student enters the room, they must sit in the seat that maximizes the distance to the closest person.
If there are multiple such seats, they sit in the seat with the lowest number.
(Also, if no one is in the room, then the student sits at seat number 0.)

Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat() returning an int
representing what seat the student sat in, and ExamRoom.leave(int p) representing that the student in seat number p
now leaves the room.  It is guaranteed that any calls to ExamRoom.leave(p) have a student sitting in seat p.

Example 1:

Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
Output: [null,0,9,4,2,null,5]
Explanation:
ExamRoom(10) -> null
seat() -> 0, no one is in the room, then the student sits at seat number 0.
seat() -> 9, the student sits at the last seat number 9.
seat() -> 4, the student sits at the last seat number 4.
seat() -> 2, the student sits at the last seat number 2.
leave(4) -> null
seat() -> 5, the student sits at the last seat number 5.

Note:

1 <= N <= 10^9
ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across all test cases.
Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting in seat number p.
*/
struct Interval
{
    int seatCount = 0;
    int left = 0;
    int right = 0;
    
    Interval(int seatCount, int left, int right)
        : seatCount(seatCount), left(left), right(right) {}
    
    // Get maximum distance to existing seat if put a seat in this interval
    int getMaxDist() const
    {
        if (left == 0) return right + 1;
        if (right == seatCount - 1) return right - left + 1;
        return static_cast<int>((right - left) / 2) + 1;
    }
    
    // Get maximum distance seat number
    int getMaxDistSeat() const
    {
        if (left == 0) return left;
        if (right == seatCount - 1) return right;
        return static_cast<int>((right + left) / 2);
    }
   
    bool operator < (const Interval& that) const
    {
        int d1 = getMaxDist();
        int d2 = that.getMaxDist();
        if (d1 != d2) return d1 > d2;
        return left < that.left;
    }
};

class ExamRoom {
public:
    int seatsCount = 0;
    std::set<Interval> intervals;
    std::unordered_map<int, int> leftToRight;
    std::unordered_map<int, int> rightToLeft;
    
    ExamRoom(int N) : seatsCount(N)
    {        
        intervals.clear();
        leftToRight.clear();
        rightToLeft.clear();
        
        addInterval(0, N - 1);
    }
    
    void addInterval(int left, int right)
    {
        if (left <= right && left >= 0 && right < seatsCount)
        {
            intervals.emplace(seatsCount, left, right);
            leftToRight[left] = right;
            rightToLeft[right] = left;
        }
    }
    
    void removeInterval(int left, int right)
    {
        if (left <= right && left >= 0 && right < seatsCount)
        {
            intervals.erase(Interval(seatsCount, left, right));
            leftToRight.erase(left);
            rightToLeft.erase(right);
        }
    }
                                            
    int seat()
    {
        auto interval = *(intervals.begin());
        removeInterval(interval.left, interval.right);

        int seat = interval.getMaxDistSeat();
        addInterval(interval.left, seat-1);
        addInterval(seat+1, interval.right);

        return seat;
    }
    
    void leave(int seat)
    {
        int left = rightToLeft.find(seat-1) == rightToLeft.end() ? seat : rightToLeft[seat-1];
        int right = leftToRight.find(seat+1) == leftToRight.end() ? seat : leftToRight[seat+1];
        
        removeInterval(left, seat-1);
        removeInterval(seat+1, right);

        addInterval(left, right);
    }
};
