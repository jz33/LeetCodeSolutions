'''
416. Partition Equal Subset Sum
https://leetcode.com/problems/partition-equal-subset-sum/

Given a non-empty array containing only positive integers,
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
 
Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if (total & 1) != 0:
            return False
        
        half = total >> 1
        
        dp = [True] + [False] * half
        for n in nums:
            # Each n can only be used once, so update from right
            for i in range(half, n - 1, -1):
                dp[i] = dp[i] or dp[i - n]
        
        return dp[-1]
