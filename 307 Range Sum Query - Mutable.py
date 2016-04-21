'''
Range Sum Query - Mmutable
https://leetcode.com/problems/range-sum-query-mutable/
'''
class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.nums = [0] * len(nums)
        # tree[:i] is sum of nums[0:i]
        self.tree = [0] * (len(nums) + 1)
        for i,e in enumerate(nums):
            self.update(i,e)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        diff = val - self.nums[i]
        self.nums[i] = val
        size = len(self.nums)
        tree = self.tree
        i += 1
        while i <= size:
            tree[i] += diff
            i += (i & -i)
        
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sum(j+1) - self.sum(i)

    def sum(self,i):
        r = 0
        tree = self.tree
        while i > 0:
            r += tree[i]
            i -= (i & -i)
        return r

obj = NumArray(range(10))
obj.update(6,-5)
print obj.nums
print obj.tree
print obj.sumRange(5,9)
