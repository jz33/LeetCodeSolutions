'''
410. Split Array Largest Sum
https://leetcode.com/problems/split-array-largest-sum/

Given an array which consists of non-negative integers and an integer m,
you can split the array into m non-empty continuous subarrays.
Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
'''
class Solution:
    def getSubarrayCount(self, nums: List[int], total: int) -> int:
        ctr = 1
        s = 0
        for e in nums:
            if s + e > total:
                ctr += 1
                s = e
            else:
                s += e
        return ctr
            
    def splitArray(self, nums: List[int], m: int) -> int:
        left = max(nums)
        right = sum(nums)
        minSum = right
        
        while left <= right:
            mid = left + (right - left) // 2
            
            count = self.getSubarrayCount(nums, mid)      
            if count > m:
                # Guessed sum is too small
                left = mid + 1
            else:
                # Guessed sum is large enough to make subarray count
                # less or equal to m
                minSum = mid
                right = mid - 1
                
        return minSum
