'''
992. Subarrays with K Different Integers
https://leetcode.com/problems/subarrays-with-k-different-integers/

Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

    For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].

Constraints:
    1 <= nums.length <= 2 * 104
    1 <= nums[i], k <= nums.length
'''
from collections import Counter

class SlidingWindow:
    def __init__(self):
        self.mapper = Counter()
        self.distinctCount = 0

    def add(self, e):
        c = self.mapper[e]
        if c == 0:
            self.distinctCount += 1
        self.mapper[e] += 1
    
    def pop(self, e):
        c = self.mapper[e]
        if c == 1:
            self.distinctCount -= 1
        self.mapper[e] -= 1

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        '''
        The trick of this question is to maintain 2 sliding windows.
        1st window represents the maximum sized subarray whose distinct count is K,
        2nd window represents the minimum sized subarray whose distinct count is K.
        '''
        # result
        goodCount = 0
        
        # pointer
        left1, left2 = 0, 0
        
        # window
        win1, win2 = SlidingWindow(), SlidingWindow()
        
        for val in nums:
            # add
            win1.add(val)
            win2.add(val)

            # shrink win1
            while win1.distinctCount > k:
                le = nums[left1]
                left1 += 1
                win1.pop(le)
            
            # shrink win2
            while win2.distinctCount >= k:
                le = nums[left2]
                left2 += 1
                win2.pop(le)
            
            # add the count of subarray ending in right
            goodCount += left2 - left1
                
        return goodCount
