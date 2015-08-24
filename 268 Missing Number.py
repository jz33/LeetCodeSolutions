'''
Missing Number
https://leetcode.com/problems/missing-number/
'''
def missingNumber(arr):
    """
    :type nums: List[int]
    :rtype: int
    """
    total = sum(arr);
    size = len(arr)
    expected = size * (size + 1) // 2
    return expected - total
