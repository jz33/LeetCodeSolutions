'''
713. Subarray Product Less Than K
https://leetcode.com/problems/subarray-product-less-than-k/

Given an array of integers nums and an integer k,
return the number of contiguous subarrays where the product of all the elements in the subarray
is strictly less than k.

Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.

Example 2:

Input: nums = [1,2,3], k = 0
Output: 0

Constraints:
    1 <= nums.length <= 3 * 104
    1 <= nums[i] <= 1000
    0 <= k <= 106
'''
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        result = 0
        product = 1
        left = 0
        for right, val in enumerate(nums):
            # Extend
            product *= val
            # Shrink
            while product >= k and left <= right:
                product = product / nums[left]
                left += 1
            # Value
            if product < k:
                # All subarray [left : right], [left + 1, right] ... [right - 1 : right]
                # are valid, as nums only contains positive integers
                result += right - left + 1
        return result

