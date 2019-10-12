'''
862. Shortest Subarray with Sum at Least K
https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/

Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.
If there is no non-empty subarray with sum at least K, return -1.
 
Example 1:

Input: A = [1], K = 1
Output: 1

Example 2:

Input: A = [1,2], K = 4
Output: -1

Example 3:

Input: A = [2,-1,2], K = 3
Output: 3
'''
from collections import deque

class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:
        '''
        Similar method to Sliding Window Maximum
        '''
        size = len(A)
        res = size + 1 # impossible value
        
        # sumArr[i] is the sum of A[:i+1]
        sumArr= [0] * (size + 1)
        for i in range(size):
            sumArr[i+1] = sumArr[i] + A[i]
        
        queue = deque()        
        for i, s in enumerate(sumArr):
            # The queue is ascending
            # If a new value s is smaller than last value of queue,
            # we can dump last value of queue, because the subarray
            # between future i and current i will have bigger sum and
            # smaller size
            while queue and s <= sumArr[queue[-1]]:
                queue.pop()

            # Try update result using front of queue
            # Front of queue and i can compose the subarray with largest
            # sum. If that sum is smaller than K, no more element is queue
            # will get the result
            while queue and s - sumArr[queue[0]] >= K:
                j = queue.popleft()               
                res = min(res, i-j)

            queue.append(i)

        return res if res != size + 1 else -1
