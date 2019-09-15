'''
239. Sliding Window Maximum
https://leetcode.com/problems/sliding-window-maximum/

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right.
You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7] 
Explanation: 

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
'''
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0: return []
        res = [None] * (len(nums) - k + 1)
        
        # dq is descending, means dq[0] is the max
        dq = deque()
        for i,e in enumerate(nums):
            # Build the desceding deque
            while len(dq) > 0 and nums[i] > nums[dq[-1]]:
                dq.pop()

            # Pop left the out of bound indexes
            while len(dq) > 0 and dq[0] <= i - k:
                dq.popleft()

            dq.append(i)
            
            if i >= k - 1:
                res[i - k + 1] = dq[0]
     
        res[-1] = dq[0]
        return [nums[i] for i in res]
