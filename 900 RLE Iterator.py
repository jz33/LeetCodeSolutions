'''
900. RLE Iterator
https://leetcode.com/problems/rle-iterator/

Write an iterator that iterates through a run-length encoded sequence.

The iterator is initialized by RLEIterator(int[] A), where A is a run-length encoding of some sequence.
More specifically, for all even i, A[i] tells us the number of times that
the non-negative integer value A[i+1] is repeated in the sequence.

The iterator supports one function: next(int n), which exhausts the next n elements (n >= 1) and returns
the last element exhausted in this way.  If there is no element left to exhaust, next returns -1 instead.

For example, we start with A = [3,8,0,9,2,5], which is a run-length encoding of the sequence [8,8,8,5,5].
This is because the sequence can be read as "three eights, zero nines, two fives".


Example 1:

Input: ["RLEIterator","next","next","next","next"], [[[3,8,0,9,2,5]],[2],[1],[1],[2]]
Output: [null,8,8,5,-1]
Explanation: 
RLEIterator is initialized with RLEIterator([3,8,0,9,2,5]).
This maps to the sequence [8,8,8,5,5].
RLEIterator.next is then called 4 times:

.next(2) exhausts 2 terms of the sequence, returning 8.  The remaining sequence is now [8, 5, 5].

.next(1) exhausts 1 term of the sequence, returning 8.  The remaining sequence is now [5, 5].

.next(1) exhausts 1 term of the sequence, returning 5.  The remaining sequence is now [5].

.next(2) exhausts 2 terms, returning -1.  This is because the first term exhausted was 5,
but the second term did not exist.  Since the last term exhausted does not exist, we return -1.
'''
class RLEIterator:
    def __init__(self, A: List[int]):
        self.intervals = []        
        if not A:
            return
        
        intervals = [] # [(start index, value)]
        startIndex = 0
        for i in range(0, len(A), 2):
            c = A[i]
            if c != 0:
                v = A[i+1]
                intervals.append((startIndex,v))
                startIndex += c
        intervals.append((startIndex, None)) # tail
        
        self.intervals = intervals
        self.used = 0

    def next(self, n: int) -> int:
        if not self.intervals:
            return -1
        
        target = self.used + n - 1
        self.used += n
        
        if target >= self.intervals[-1][0]:
            return -1

        # Binary search on insertion point
        arr = self.intervals
        left = 0
        right = len(arr) - 1
        foundIndex = None
        
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid][0] == target:
                foundIndex = mid
                break
            elif arr[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        if foundIndex is None:
            return arr[left-1][1] # left is insertion point
        else:
            return arr[foundIndex][1]        
