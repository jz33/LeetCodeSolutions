'''
480. Sliding Window Median
https://leetcode.com/problems/sliding-window-median/

Median is the middle value in an ordered integer list.
If the size of the list is even, there is no middle value.
So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving
from the very left of the array to the very right. You can only see the k numbers in the window.
Each time the sliding window moves right by one position.
Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note:
You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array.
'''
from sortedcontainers import SortedList
# http://www.grantjenks.com/docs/sortedcontainers/#api-documentation

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        result = []
        window = SortedList()

        for i, e in enumerate(nums):
            window.add(nums[i])
            if i >= k:
                window.remove(nums[i - k])
                
            if i >= k - 1:
                if (k & 1) == 1:
                    result.append(window[k >> 1])
                else:
                    result.append((window[k >> 1] + window[(k >> 1) - 1]) / 2.0)
                
        return result
