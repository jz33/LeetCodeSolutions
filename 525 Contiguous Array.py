'''
525. Contiguous Array
https://leetcode.com/problems/contiguous-array/

Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Constraints:
    1 <= nums.length <= 105
    nums[i] is either 0 or 1.
'''
class Solution:
    '''
    Similar idea to 523. Continuous Subarray Sum
    '''
    def findMaxLength(self, nums: List[int]) -> int:
        book = {0 : -1} # {count of total zeros - total ones : first appeared index}
        zeros = 0
        ones = 0
        longest = 0
        for i, e in enumerate(nums):
            if e == 0:
                zeros += 1
            else:
                ones += 1
            j = book.get(zeros - ones)
            if j is not None:
                longest = max(longest, i - j)
            else:
                book[zeros - ones] = i
        return longest
