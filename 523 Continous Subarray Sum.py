'''
523. Continuous Subarray Sum
Given a list of non-negative numbers and a target integer k,
write a function to check if the array has a continuous subarray of size at least 2 that sums up to a multiple of k,
that is, sums up to n*k where n is also an integer.

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
'''
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        '''
        Idea: for nums, lets s[i] be sum of nums[0]...nums[i], then
        if j > i + 1, and s[j] % k ==  s[i] % k, then nums[i+1:j+1] is the subarray whose
        sum is multiple of k
         '''
        # {sum : index}
        # Assume sum of 0 is already there
        # Think case like [5], 5, and [5,5], 5
        ref = {0:-1}
        # local sum
        s = 0
        for i,e in enumerate(nums):
            s += e
            if k != 0: 
                s %= k
                
            j = ref.get(s)
            if j is None:
                ref[s] = i
    
            # If i - j > 1, then the subarray is [j+1:i+1]
            elif i - j > 1:
                return True

        return False
