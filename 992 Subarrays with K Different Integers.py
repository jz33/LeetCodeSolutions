'''
992. Subarrays with K Different Integers
https://leetcode.com/problems/subarrays-with-k-different-integers/

Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if
the number of different integers in that subarray is exactly K.

(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)

Return the number of good subarrays of A.

Example 1:

Input: A = [1,2,1,2,3], K = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].

Example 2:

Input: A = [1,2,1,3,4], K = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

Note:

1 <= A.length <= 20000
1 <= A[i] <= A.length
1 <= K <= A.length
'''
class SlidingWindow:
    def __init__(self):
        self.mapper = collections.Counter()
        self.distinctCount = 0

    def add(self, e):
        c = self.mapper[e]
        if c == 0:
            self.distinctCount += 1
        self.mapper[e] += 1
    
    def pop(self, e):
        c = self.mapper[e]
        if c == 1:
            self.distinctCount -= 1
        self.mapper[e] -= 1

class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        '''
        The trick of this question is to maintain 2 sliding windows.
        1st window represents the maximum sized subarray whose distinct count is K,
        2nd window represents the minimum sized subarray whose distince count is K.
        '''
        # result
        goodCount = 0
        
        # pointer
        left1, left2 = 0, 0
        
        # window
        win1, win2 = SlidingWindow(), SlidingWindow()
        
        for right, val in enumerate(A):
            # add
            win1.add(val)
            win2.add(val)

            # shrink win1
            while win1.distinctCount > K:
                le = A[left1]
                left1 += 1
                win1.pop(le)
            
            # shrink win2
            while win2.distinctCount >= K:
                le = A[left2]
                left2 += 1
                win2.pop(le)
            
            # add the count of subarray ending in right
            goodCount += left2 - left1
                
        return goodCount
