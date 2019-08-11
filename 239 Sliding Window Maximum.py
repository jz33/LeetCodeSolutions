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
