'''
Missing Ranges
https://leetcode.com/problems/missing-ranges/
'''
def findMissingRanges(self, nums, lower, upper):
    """
    :type nums: List[int]
    :type lower: int
    :type upper: int
    :rtype: List[str]
    """
    res = []
    j = lower
    for i,e in enumerate(nums):
        if e > j:
            if j == e - 1:
                res.append(str(j))
            else:
                res.append(str(j)+'->'+str(e - 1))
        j = e + 1
    if j == upper:
        res.append(str(j))
    elif j < upper:
        res.append(str(j)+'->'+str(upper))
    return res
