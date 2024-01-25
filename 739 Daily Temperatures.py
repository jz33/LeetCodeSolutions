'''
739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/

Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait
after the ith day to get a warmer temperature.

If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
    1 <= temperatures.length <= 105
    30 <= temperatures[i] <= 100
'''
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # indexes of previous temperatures
        for ti, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                lastTempIndex = stack.pop()
                result[lastTempIndex] = ti - lastTempIndex
            stack.append(ti)
        return result

class Solution2:
    '''
    O(N) without stack
    Real TikTok question: https://www.1point3acres.com/bbs/thread-1018530-1-1.html
    '''
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        hottestTemp = temperatures[-1]
        for day in range(len(temperatures)-1, -1, -1):
            temp = temperatures[day]
            if temp >= hottestTemp:
                # If current temperature is the hottest from now on, there is no answer at i.
                hottestTemp = temp
            else:
                # Keep finding the higher temp day on right, using existing results.
                # As the lookup is jumping, total lookup time won't exceed N
                # No need to check boundary of higherDay as current temp is not hottest
                higherDay = day + 1
                while temperatures[higherDay] <= temp:
                    higherDay += result[higherDay]
                result[day] = higherDay - day
        return result

