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
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = collections.deque()
        res = []
         
        for i,c in enumerate(nums):
            # dq is descending, dq[0] is the max of current substring
            while dq and c > nums[dq[-1]]:
                dq.pop()
            
            # pop the out of bound indexes
            # i-k+1 is the smallest index of current substring
            while dq and i-k+1 > dq[0]:
                dq.popleft()
                
            dq.append(i)
            
            if i-k+1 >= 0:
                res.append(nums[dq[0]])
                
        return res
