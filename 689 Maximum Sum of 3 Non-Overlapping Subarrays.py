'''
689. Maximum Sum of 3 Non-Overlapping Subarrays
https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

In a given array nums of positive integers, find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the sum of all 3*k entries.

Return the result as a list of indices representing the starting position of each interval (0-indexed).
If there are multiple answers, return the lexicographically smallest one.

Example:

Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
 
Note:

nums.length will be between 1 and 20000.
nums[i] will be between 1 and 65535.
k will be between 1 and floor(nums.length / 3).
'''
def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
    '''
    Solution based on Best Time to Buy and Sell Stock IV
    '''
    sums = [0] * (len(nums) + 1)
    for i, e in enumerate(nums):
        sums[i + 1] = sums[i] + e
    
    # Let i be index of nums array
    # Let j be iterator of count of subarrays (which is 3), aka, selection times
    # So at i,j, if select nums[i], total value will be: dp[i-k][j-1] + Sum(nums[i...i-k]) 
    # If not select nums[i] total will be dp[i-1][j]
    # Therefore dp[i][j] is max of them

    # Notice we need to remember indexes too, let
    # dp[i][j][0] stores the sum, dp[i][j][1] stores the starting indexes list
    dp = [[(0, [])] * 4 for _ in range(len(nums)+1)]
    for i in range(k, len(nums)+1):
        for j in range(1, 4):

            selected = dp[i-k][j-1][0] + sums[i] - sums[i-k]
            unSelected = dp[i-1][j][0]

            # Not >=, as we prefer earlier indexes
            if selected > unSelected:
                dp[i][j] = (selected, dp[i-k][j-1][1] + [i-k])
            else:
                dp[i][j] = (unSelected, dp[i-1][j][1])

    return dp[-1][-1][1]
