'''
Burst Balloons
https://leetcode.com/problems/burst-balloons/
'''
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        n = len(nums)
        
        # dp[i][j] is max value in [i+1,j-1]
        dp = [[0 for _ in xrange(n)] for _ in xrange(n)]
        
        for gap in xrange(2,n):
            for i in xrange(n - gap):
                j = i + gap
                for k in xrange(i+1,j):
                    dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j]+nums[i]*nums[k]*nums[j])
        for row in dp:
            print row
        return dp[0][n-1]
        
sol = Solution()
nums = [1,2,3,4,5]
print sol.maxCoins(nums)
