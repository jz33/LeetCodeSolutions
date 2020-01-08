'''
719. Find K-th Smallest Pair Distance
https://leetcode.com/problems/find-k-th-smallest-pair-distance/

Given an integer array, return the k-th smallest distance among all the pairs.
The distance of a pair (A, B) is defined as the absolute difference between A and B.

Example 1:
Input:
nums = [1,3,1]
k = 1
Output: 0 

Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0

Note:
2 <= len(nums) <= 10000.
0 <= nums[i] < 1000000.
1 <= k <= len(nums) * (len(nums) - 1) / 2.
'''
class Solution:
    def countDistancesSmallerOrEqual(self, nums: List[int], targetDist: int) -> int:
        j = 1
        ct = 0
        for i in range(len(nums)):
            while j < len(nums) and nums[j] - nums[i] <= targetDist:
                j += 1
            ct += j - i - 1
        return ct
            
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        leftDist = 0
        rightDist = 1000000
        while leftDist < rightDist:
            midDist = leftDist + (rightDist - leftDist) // 2
            
            ctr = self.countDistancesSmallerOrEqual(nums, midDist)         
            if ctr < k:
                leftDist = midDist + 1
            else: # if ctr == k, midDist is a candidate
                rightDist = midDist
                
        return leftDist
