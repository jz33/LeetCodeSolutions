'''
525. Contiguous Array
https://leetcode.com/problems/contiguous-array/

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:

Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.
Example 2:

Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
Note: The length of the given binary array will not exceed 50,000.
'''
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        book = {0 : -1} # {count of total zeros - total ones : earliest index}
        zeros = 0
        ones = 0
        longest = 0
        for i,e in enumerate(nums):
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
