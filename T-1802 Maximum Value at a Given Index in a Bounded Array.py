'''
1802. Maximum Value at a Given Index in a Bounded Array
https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/

You are given three positive integers: n, index, and maxSum.
You want to construct an array nums (0-indexed) that satisfies the following conditions:

    nums.length == n
    nums[i] is a positive integer where 0 <= i < n.
    abs(nums[i] - nums[i+1]) <= 1 where 0 <= i < n-1.
    The sum of all the elements of nums does not exceed maxSum.
    nums[index] is maximized.

Return nums[index] of the constructed array.

Note that abs(x) equals x if x >= 0, and -x otherwise.

Example 1:

Input: n = 4, index = 2,  maxSum = 6
Output: 2
Explanation: nums = [1,2,2,1] is one array that satisfies all the conditions.
There are no arrays that satisfy all the conditions and have nums[2] == 3, so 2 is the maximum nums[2].

Example 2:

Input: n = 6, index = 1,  maxSum = 10
Output: 3

Constraints:
    1 <= n <= maxSum <= 109
    0 <= index < n
'''
class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        '''
        Binary guess on the largest possible value on nums[index]
        '''
        def halfSum(guessVal: int, halfSize: int) -> int:
            '''
            Get the half sum of the array from 0 to guessVal (exclusive) or
            from guessVal (exclusive)to end
            @halfSize: size of the subarray, exclusive of nums[index]
            '''
            ones = max(halfSize - (guessVal - 1), 0)
            trendSize = min(guessVal - 1, halfSize)
            trendStart = max(1, guessVal - halfSize)
            trendEnd = guessVal - 1
            return ones + (trendStart + trendEnd) * trendSize // 2

        left = 1 # minimum possible value of nums[index]
        right = maxSum # maximum possible value of nums[index]
        result = None
        while left <= right:
            mid = (left + right) // 2
            totalSum = halfSum(mid, index) + halfSum(mid, n - index - 1) + mid
            if totalSum <= maxSum:
                result = mid
                left = mid + 1
            else:
                right = mid - 1
        return result
