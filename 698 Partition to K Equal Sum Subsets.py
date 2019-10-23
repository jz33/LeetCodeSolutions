'''
698. Partition to K Equal Sum Subsets
Given an array of integers nums and a positive integer k,
find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
'''
class Solution:
    def backtrack(self, buckets: List[int], srcIndex: int) -> bool:
        '''
        Time Complexity: len(buckets) * (len(src))!
        Space Complexity: len(buckets)
        '''
        if srcIndex == len(self.src):
            return True
        
        e = self.src[srcIndex]
        for i in range(len(buckets)):
            if buckets[i] + e <= self.target:
                buckets[i] += e
                if self.backtrack(buckets, srcIndex + 1):
                    return True
                buckets[i] -= e

        return False

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if len(nums) < k:
            return False

        total = sum(nums)
        if total % k != 0:
            return False
        
        buckets = [0] * k

        # We want to fit larger elements to bucket earlier, so sort reversely
        self.src = sorted(nums, reverse=True)
        self.target = total // k # Subset sum target
        
        return self.backtrack(buckets, 0)
