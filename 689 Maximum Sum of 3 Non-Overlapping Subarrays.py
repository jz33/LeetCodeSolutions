'''
689. Maximum Sum of 3 Non-Overlapping Subarrays
https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/

Given an integer array nums and an integer k,
find three non-overlapping subarrays of length k with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval (0-indexed).
If there are multiple answers, return the lexicographically smallest one.

Example 1:

Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0,3,5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.

Example 2:

Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
Output: [0,2,4]

Constraints:
    1 <= nums.length <= 2 * 104
    1 <= nums[i] < 216
    1 <= k <= floor(nums.length / 3)
'''
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # 1. Compute sums of all k-sized ranges, using sliding window
        kSums = []
        total = 0
        for i, v in enumerate(nums):
            total += v
            if i - k >= 0:
                total -= nums[i-k]
            if i - k + 1 >= 0:
                kSums.append(total)
        
        # 2. Similar to 42. Trapping Rain Water, from both directions, get the max heights index arrays
        leftMaxSums = [None] * len(kSums)
        maxIndex = 0
        for i, s in enumerate(kSums):
            if s > kSums[maxIndex]:
                maxIndex = i
            leftMaxSums[i] = maxIndex

        rightMaxSums = [None] * len(kSums)
        maxIndex = len(kSums) - 1
        for i in range(len(kSums)-1, -1, -1):
            s = kSums[i]
            # Not s > kSums[maxIndex] as we want smaller index
            if s >= kSums[maxIndex]:
                maxIndex = i
            rightMaxSums[i] = maxIndex

        # 3. Compute result [x, y, z] by iterating all y, and get x, z from leftMaxSums and rightMaxSums
        result = None
        for y in range(k, len(kSums)-k):
            x = leftMaxSums[y - k]
            z = rightMaxSums[y + k]
            if result is None:
                result = [x,y,z]
            else:
                oldTotal = kSums[result[0]] + kSums[result[1]] + kSums[result[2]]
                newTotal = kSums[x] + kSums[y] + kSums[z]
                if newTotal > oldTotal:
                    result = [x,y,z]
        return result

class Solution2:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]: 
        '''
        Solution based on 188. Best Time to Buy and Sell Stock IV
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

                # If select subarray nums[i-k...i], total sum is:
                selected = dp[i-k][j-1][0] + sums[i] - sums[i-k]
            
                # If not select subarray nums[i-k...i], total sum is:
                unSelected = dp[i-1][j][0]

                # Not >=, as we prefer earlier indexes
                if selected > unSelected:
                    dp[i][j] = (selected, dp[i-k][j-1][1] + [i-k])
                else:
                    dp[i][j] = (unSelected, dp[i-1][j][1])

        return dp[-1][-1][1]
