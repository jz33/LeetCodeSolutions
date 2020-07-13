'''
1. Two Sum
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        @nums is not sorted, indicates hash map
        '''
        seen = {} # {seen number : index}
        for index, val in enumerate(nums):
            found = seen.get(target - val)
            if found is not None:
                return [found,index]
            seen[val] = index     
        return None # not reachable for this question
