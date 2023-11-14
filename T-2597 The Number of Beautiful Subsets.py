'''
2597. The Number of Beautiful Subsets
https://leetcode.com/problems/the-number-of-beautiful-subsets/

You are given an array nums of positive integers and a positive integer k.

A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.

Return the number of non-empty beautiful subsets of the array nums.

A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums.
Two subsets are different if and only if the chosen indices to delete are different.
 
Example 1:

Input: nums = [2,4,6], k = 2
Output: 4
Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
It can be proved that there are only 4 beautiful subsets in the array [2,4,6].

Example 2:

Input: nums = [1], k = 1
Output: 1
Explanation: The beautiful subset of the array nums is [1].
It can be proved that there is only 1 beautiful subset in the array [1].

Constraints:

    1 <= nums.length <= 20
    1 <= nums[i], k <= 1000
'''
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        counter = collections.Counter(nums)
        # If sort nums, at an index j, to consider a previous index i
        # it needs to look around i to find an index that has diff to nums[j] as k.
        # Therefore, to avoid forward or backend looking, group the numbers by remainder of k
        groups = [[] for _ in range(k)]
        for key in counter.keys():
            groups[key % k].append(key)

        # Compute each group's valid subsets count (including the empty subset),
        # then times then together will be the answer + the total empty subset
        def subsetsCount(group: List[int]) -> int:
            # Considering empty subset as valid
            if len(group) == 0:
                return 1
            # The dp[i] means the # of valid subsets ended on i (the arr[i] can either be selected or not)
            # Similar to 198. House Robber
            dp = [None, None, 1]
            # Considering dups, the value on selecting a num or not is pow(2, frequency)
            dp[0] = pow(2, counter[group[0]])
            for i in range(1, len(group)):
                di = i % 3
                multiplier = pow(2, counter[group[i]])
                if group[i] - group[i-1] == k:
                    # Can only choose group[i] (dp[i-2]), or no group[i] (dp[i-1])
                    dp[di] = dp[di-1] + dp[di-2] * (multiplier - 1)
                else:
                    # Can choose based on dp[i-1], and choose group[i] or not
                    dp[di] = dp[di-1] * multiplier
            return dp[(len(group)-1) % 3]

        result = 1
        for group in groups:
            result *= subsetsCount(sorted(group))
        return result - 1
