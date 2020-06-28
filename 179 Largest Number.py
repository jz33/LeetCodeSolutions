'''
179. Largest Number
https://leetcode.com/problems/largest-number/

Given a list of non negative integers,
arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"

Example 2:

Input: [3,30,34,5,9]
Output: "9534330"

Note: The result may be very large, so you need to return a string instead of an integer.
'''
class Comparable:
    def __init__(self, num):
        self.val = str(num)

    def __lt__(self, that):
        # '82' is before '824' because '82|824' is greater than '824|82'
        return self.val + that.val > that.val + self.val

class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        strs = [Comparable(n) for n in nums]
        strs.sort()
        
        res = ''.join((n.val for n in strs))
        return res.lstrip('0') or '0'
