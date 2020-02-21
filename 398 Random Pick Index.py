'''
398. Random Pick Index
https://leetcode.com/problems/random-pick-index/

Given an array of integers with possible duplicates, randomly output the index of a given target number.
You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
'''
from random import randint

class Solution:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        resIndex = -1
        count = 0
        for i, e in enumerate(self.nums):
            if e == target:
                count += 1
                if randint(1, count) == 1:
                    resIndex = i
        return resIndex
