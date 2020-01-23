'''
163. Missing Ranges
https://leetcode.com/problems/missing-ranges/

Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper],
return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]
'''
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        i = lower
        for e in nums:
            if i < e:
                if i == e - 1:
                    res.append(str(i))
                else:
                    res.append(str(i)+'->'+str(e - 1))
            i = e + 1
            
        if i == upper:
            res.append(str(i))
        elif i < upper:
            res.append(str(i)+'->'+str(upper))
            
        return res
