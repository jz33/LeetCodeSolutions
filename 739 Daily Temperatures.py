'''
739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/

Given a list of daily temperatures T, return a list such that, for each day in the input,
tells you how many days you would have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73],
your output should be [1, 1, 4, 2, 1, 1, 0, 0].
'''
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = [] # descending indexes
        for i, t in enumerate(T):
            while stack and t > T[stack[-1]]:
                last = stack.pop()
                res[last] = i - last
            stack.append(i) 
        return res
