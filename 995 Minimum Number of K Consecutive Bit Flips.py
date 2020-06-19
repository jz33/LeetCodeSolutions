'''
995. Minimum Number of K Consecutive Bit Flips
https://leetcode.com/problems/set-intersection-size-at-least-two/

In an array A containing only 0s and 1s, a K-bit flip consists of choosing a (contiguous) subarray of length K and
simultaneously changing every 0 in the subarray to 1, and every 1 in the subarray to 0.

Return the minimum number of K-bit flips required so that there is no 0 in the array.
If it is not possible, return -1.

Example 1:

Input: A = [0,1,0], K = 1
Output: 2
Explanation: Flip A[0], then flip A[2].

Example 2:

Input: A = [1,1,0], K = 2
Output: -1
Explanation: No matter how we flip subarrays of size 2, we can't make the array become [1,1,1].

Example 3:

Input: A = [0,0,0,1,0,1,1,0], K = 3
Output: 3
Explanation:
Flip A[0],A[1],A[2]: A becomes [1,1,1,1,0,1,1,0]
Flip A[4],A[5],A[6]: A becomes [1,1,1,1,1,0,0,0]
Flip A[5],A[6],A[7]: A becomes [1,1,1,1,1,1,1,1]

Note:

1 <= A.length <= 30000
1 <= K <= A.length
'''
from collections import deque

class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        flipIndexes = deque()
        flipCount = 0
        for i, e in enumerate(A):
            # Pop-up out of bound flip indexes
            if flipIndexes and flipIndexes[0] <= i - K:
                flipIndexes.popleft()
            
            # Now size of flipIndexes is # of flips applied on A[i]
            # Check if A[i] after these flips is 0 or 1
            if (e ^ (len(flipIndexes) & 1)) == 0:
                if len(A) - i < K:
                    # If remaining length is less than K, cannot flip
                    return -1
                    
                flipCount += 1
                flipIndexes.append(i)

        return flipCount
