'''
41. First Missing Positive
https://leetcode.com/problems/first-missing-positive/

Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:

Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.

Example 3:

Input: nums = [7,8,9,11,12]
Output: 1
Explanation: The smallest positive integer 1 is missing.

Constraints:
    1 <= nums.length <= 105
    -231 <= nums[i] <= 231 - 1
'''
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            # Swap a positive into its right place, for example, 3 should be put into index 2
            # Do this in while loop, because nums[nums[i]-1] might need to be swapped too.
            # This runs in O(n) as each number is swapped at most once
            while nums[i] > 0 and nums[i] <= len(nums) and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
            
        # Check from beginning
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        else:
            return len(nums) + 1

   
'''
Real facebook question:
第二题 输入是一个数组和数字n, 如果数组里正好有1到n的整数输出true否则false
https://www.1point3acres.com/bbs/thread-1041414-1-1.html
'''
def checkN(arr: List[int], n: int) -> bool:
    if len(arr) != n:
        # 1. Not same length
        return False
    
    for i in range(n):
        # Find the right element for index i
        while arr[i] != i + 1:
            if not 1 <= arr[i] <= n:
                # 2. The element is out of bound
                return False
        
            right = arr[i] - 1
            if arr[right] == arr[i]:
                # 3. Duplicates
                return False
            
            arr[right], arr[i] = arr[i], arr[right]

    return True

cases = [
    [1,2,3,4,5],
    [5,4,3,2,1],
    [1,1,1,3,2],
    [5,4,1,3,6],
    [5,4,2,3,7],
    [4,3,1,5,2],
]
for case in cases:
    # Interesting enough, Python executes the part inside 'format' first, so
    # the input array is changed
    print('input: {0}, output: {1}'.format(case, checkN(case, len(case))))