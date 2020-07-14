'''
18. 4Sum
https://leetcode.com/problems/4sum/

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that
a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''
class Solution:
    def twoSum(self, nums: List[int], left: int, right: int, target: int):
        '''
        return value pairs, handle duplicates
        '''
        def moveLeft():
            nonlocal left
            left += 1
            while left < right and nums[left] == nums[left - 1]:
                left += 1
                
        def moveRight():
            nonlocal right
            right -= 1
            while right > left and nums[right] == nums[right + 1]:
                right -= 1
                
        result = []
        while left < right:
            total = nums[left] + nums[right]
            if total == target:
                result.append([nums[left], nums[right]])
                moveLeft()
                moveRight()
            elif total < target:
                moveLeft()
            else:
                moveRight()
        return result
            
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)-3):
            # Handle duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            for j in range(i+1, len(nums)-2):
                # Handle duplicates
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                
                remain = target - nums[i] - nums[j]
                twoSumResult = self.twoSum(nums, j+1, len(nums)-1, remain)
                if twoSumResult:
                    for r in twoSumResult:
                        result.append([nums[i], nums[j]] + r)
        return result
