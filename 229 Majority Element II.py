'''
229. Majority Element II
https://leetcode.com/problems/majority-element-ii/

Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:

Input: [3,2,3]
Output: [3]

Example 2:

Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
'''
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums
        
        count = [0, 0]
        major = [0, 1]
        for n in nums:
            if n == major[0]:
                count[0] += 1
            elif n == major[1]:
                count[1] += 1
            elif count[0] == 0:
                count[0], major[0] = 1, n
            elif count[1] == 0:
                count[1], major[1] = 1, n
            else:
                count = [count[0] - 1, count[1] - 1]
        
        return [m for m in major if nums.count(m) > len(nums) // 3]
