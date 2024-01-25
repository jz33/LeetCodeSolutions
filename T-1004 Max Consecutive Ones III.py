'''
1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/

Given a binary array nums and an integer k,
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Constraints:
    1 <= nums.length <= 105
    nums[i] is either 0 or 1.
    0 <= k <= nums.length
'''
class Solution:
    '''
    Real facebook interview question: 
    https://www.1point3acres.com/bbs/thread-1040708-1-1.html
    
    Similar sliding window pattern like 3. Longest Substring Without Repeating Characters
    The question is equivalent to ask: what's the longest substring
    with at most k zeros ?
    '''
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxLength = 0
        zeroCount = 0
        left = 0 # left index of the sliding window
        for right, val in enumerate(nums):
            if val == 0:
                zeroCount += 1
                while zeroCount > k:
                    # If more than k zeros in the window, shrink from left
                    if nums[left] == 0:
                        zeroCount -= 1
                    left += 1
            maxLength = max(maxLength, right - left + 1)

        # Calculate last window size as i is out of bound
        maxLength = max(maxLength, len(nums) - left)
        return maxLength
