import sys

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3: return False
        first = nums[0]
        second = sys.maxint
        for i in xrange(1,len(nums)):
            e = nums[i]
            if e <= first:
                first = e
            elif e <= second:
                second = e
            elif e > second:
                return True
        return False
