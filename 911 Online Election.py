'''
911. Online Election
https://leetcode.com/problems/online-election/

In an election, the i-th vote was cast for persons[i] at time times[i].

Now, we would like to implement the following query function:
TopVotedCandidate.q(int t) will return the number of the person that was leading the election at time t.  

Votes cast at time t will count towards our query.
In the case of a tie, the most recent vote (among tied candidates) wins.

Example 1:

Input: ["TopVotedCandidate","q","q","q","q","q","q"], [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
Output: [null,0,1,1,0,0,1]
Explanation: 
At time 3, the votes are [0], and 0 is leading.
At time 12, the votes are [0,1,1], and 1 is leading.
At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the most recent vote.)
This continues for 3 more queries at time 15, 24, and 8.
 
Note:

1 <= persons.length = times.length <= 5000
0 <= persons[i] <= persons.length
times is a strictly increasing array with all elements in [0, 10^9].
TopVotedCandidate.q is called at most 10000 times per test case.
TopVotedCandidate.q(int t) is always called with t >= times[0].
'''
from collections import Counter

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        ctr = Counter()
        size = len(persons)
        most = [-1, float('-inf')] # [Most voted person, most voted count]
        arr = [] # [(timestamp, most voted person)]
        for i in range(size):
            p = persons[i]
            t = times[i]
            ctr[p] += 1
            if ctr[p] >= most[1]:
                most = [p, ctr[p]]
            arr.append((t, most[0]))            
        self.arr = arr
          
    def insertionPoint(self, targetTimestamp: int):   
        arr = self.arr
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid][0] == targetTimestamp:
                return True, mid
            
            if arr[mid][0] < targetTimestamp:
                left = mid + 1
            else:
                right = mid - 1
        return False, left
        
    def q(self, t: int) -> int:
        arr = self.arr
        found, i = self.insertionPoint(t)
        if found:
            return arr[i][1]
        else:
            return arr[i-1][1]
