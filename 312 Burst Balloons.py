'''
312. Burst Balloons
https://leetcode.com/problems/burst-balloons/

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums.
You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins.
Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100

Example:

Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
             
'''
class Solution:
    '''
    Bottom-up method, 3D
    '''
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        
        # dp[i][j] is the max value in nums[i:j]
        dp = [[0] * n for _ in range(n)]
        
        # The building dp order:
        # [0,2], [1,3], ...
        # [0,3], [1,4], ...
        # Therefore step is from 2 to n
        for step in range(2, n):
            for left in range(n - step):
                right  = left + step
                for i in range(left+1,right):
                    dp[left][right] = max(dp[left][right], dp[left][i]+dp[i][right]+nums[left]*nums[i]*nums[right])
   
        return dp[0][n-1]

  
from functools import lru_cache

class Solution:
    '''
    Top-down method
    '''
    @lru_cache(None)
    def topDown(self, left: int, right: int) -> int:
        '''
        @left and right are inclusive indexes 
        '''
        if left > right:
            return 0
        
        nums = self.nums
        result = 0
        if left == right:
            result = nums[left-1] * nums[left] * nums[left+1]
        else:
            # Try burst balloon from left to right.
            # If i is burst, the cost is equal to dp[left...i-1] + dp[i+1...right]
            # plus nums[left-1] * nums[i] * nums[right+1], because balloons in 
            # [left...i-1] and [i+1...right] are all gone.
            result = max(nums[i] * nums[left-1] * nums[right+1] + \
                         self.topDown(left, i-1) + self.topDown(i+1, right) \
                         for i in range(left, right+1))
                
        return result     
    
    def maxCoins(self, nums: List[int]) -> int:
        self.nums = [1] + nums + [1]
        return self.topDown(1, len(self.nums)-2)
