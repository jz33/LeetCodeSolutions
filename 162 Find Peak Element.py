'''
162. Find Peak Element
https://leetcode.com/problems/find-peak-element/

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index.
If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words,
an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2,
or index number 5 where the peak element is 6.

Constraints:
    1 <= nums.length <= 1000
    -231 <= nums[i] <= 231 - 1
    nums[i] != nums[i + 1] for all valid i
'''
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid+1]:
                # Needs to go left, mid can be the peak
                right = mid
            else: # nums[mid] < nums[mid+1]
                # Needs to go right, mid cannot be peak, mid+1 can
                left = mid + 1             
        # left == right
        return left
    
'''
Facebook interview: find local min

第二道：要留二变体，给一个数组，只需要找到其中一个元素比它左右两边的元素小就可以，如果有多个结果只需返回其中一个。
如果在中间找不到的话，查看第一个或者最后一个元素也可

https://www.1point3acres.com/bbs/thread-1043199-1-1.html
https://www.1point3acres.com/bbs/thread-1041991-1-1.html
'''
def findMinElement(nums: List[int]) -> int:
    if not nums:
        return None
    if len(nums) < 2:
        return nums[0]
    
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > nums[mid+1]:
            # Needs to go right, mid cannot be the min
            left = mid + 1
        else: # nums[mid] < nums[mid+1]
            # Needs to go left, mid can be min, mid+1 cannot
            right = mid            
    # left == right
    return left
