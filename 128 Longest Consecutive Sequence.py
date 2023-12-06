'''
128 Longest Consecutive Sequence.py
https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers nums,
return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        # Only needs set not hashmap, as it is asking the sequence not substring
        seen = set(nums) 
        while seen:
            value = seen.pop()
            print(value)
            # Expand from value
            count = 1
            pointer = value
            while pointer - 1 in seen:
                count += 1
                pointer -= 1
                seen.remove(pointer)
            pointer = value
            while pointer + 1 in seen:
                count += 1
                pointer += 1
                seen.remove(pointer)
            result = max(result, count)      
        return result
