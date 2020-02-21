'''
https://leetcode.com/discuss/interview-question/451431/Facebook-or-Onsite-or-Generate-random-max-index

Given an array of integers arr, randomly return an index of the maximum value seen by far.

Example:
Input: [11, 30, 2, 30, 30, 30, 6, 2, 62, 62]

Having iterated up to the at element index 5 (where the last 30 is),
randomly give an index among [1, 3, 4, 5] which are indices of 30 - the max value by far. 
Each index should have a ¼ chance to get picked.

Having iterated through the entire array, randomly give an index between 8 and 9 which are indices of the max value 6
'''
from typing import List
from random import randint

class Solution:
    def reservoirSample(self, arr: List[int]) -> List[int]:
        maxInt = float('-inf')
        maxIndex = -1
        maxCount = 0
        res = []
        for i, e in enumerate(arr):
            if e > maxInt:
                maxInt = e
                maxIndex = i
                maxCount = 1
            elif e == maxInt:
                maxCount += 1

                if randint(1, maxCount) == 1:
                    maxIndex = i

            res.append(maxIndex)
        return res


sol = Solution()
arr = [11, 30, 2, 30, 30, 30, 6, 2, 62, 62]
print(sol.reservoirSample(arr))
