'''
644. Maximum Average Subarray II
https://leetcode.com/problems/maximum-average-subarray-ii/

Given an array consisting of n integers, find the contiguous subarray whose length is greater than or equal to k
that has the maximum average value. And you need to output the maximum average value.

Example 1:

Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation:
when length is 5, maximum average value is 10.8,
when length is 6, maximum average value is 9.16667.
Thus return 12.75.

Note:

1 <= k <= n <= 10,000.
Elements of the given array will be in range [-10,000, 10,000].
The answer with the calculation error less than 10-5 will be accepted.
'''
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # Build prefix sum
        prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix[i+1] = prefix[i] + nums[i]
        
        def getAvg(x, y):
            # Get average of nums[x : y]
            return (prefix[y] - prefix[x]) / (y - x)
        
        # The queue stores the "left" indexes of subarray
        queue = collections.deque()
        maxAvg = float('-inf')
        for i in range(k - 1, len(nums)):
            # So, for each iteration, current average is: getAvg(queue[0], i + 1)
            # The idea is to select proper queue[0] which makes above equation as big as possible.
            
            # The average of nums[queue[-2] : queue[-1]] is bigger than nums[queue[-2] : queue[left]]
            # then discard queue[-1] as use queue[-2] as left bound can get bigger average
            while len(queue) >= 2 and getAvg(queue[-2], queue[-1]) >= getAvg(queue[-2], i - k + 1):
                queue.pop()
            
            # i - k + 1 is the current left index of subarray [i-k+1 : i+1]
            # Add current left so next line can do pop
            queue.append(i - k + 1)
            
            # The average of nums[queue[0] : queue[1]] is smaller nums[queue[0] : i+1]
            # then discard queue[0], because nums[queue[1] : i+1] must have bigger average.
            while len(queue) >= 2 and getAvg(queue[0], queue[1]) <= getAvg(queue[0], i + 1):
                queue.popleft()
                
            maxAvg = max(maxAvg, getAvg(queue[0], i + 1))

        return maxAvg
