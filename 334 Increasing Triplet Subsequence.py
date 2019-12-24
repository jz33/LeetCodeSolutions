'''
334. Increasing Triplet Subsequence
https://leetcode.com/problems/increasing-triplet-subsequence/

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k 
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false
'''
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        '''
        A special case for 300. Longest Increasing Subsequence
        '''
        if len(nums) < 3:
            return False
        
        first = nums[0]
        second = float('inf')
        for i in range(1, len(nums)):
            e = nums[i]
            if e <= first: # not <
                first = e
            elif e <= second:
                second = e
            else:
                return True
        return False
