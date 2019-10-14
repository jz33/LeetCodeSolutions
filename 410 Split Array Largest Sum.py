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
    '''
    A special binary search method
    '''
    def splitArray(self, nums: List[int], m: int) -> int:
        size = len(nums)
        
        # left is max of array, which is smallest possible return
        left = max(nums) 
        # right is sum of array, which is largest possible return
        right = sum(nums)   
        res = right

        while left <= right:
            middle = left + ((right - left) >> 1);

            # Count maximum number of subarrays whose sum is <= middle
            localSum = 0
            counter = 1
            for i in range(size):
                localSum += nums[i]
                if localSum > middle:
                    counter += 1
                    localSum = nums[i]

            if counter <= m:
                res = min(res, middle)
                right = middle - 1
            else:
                left = middle + 1

        return res
