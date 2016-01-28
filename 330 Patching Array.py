'''
330 Patching Array
https://leetcode.com/problems/patching-array/
'''
def minPatches(nums, n):
    """
    :type nums: List[int]
    :type n: int
    :rtype: int
    """
    size = len(nums)
    i = 0 # position in nums
    bound = 1 # next required bound
    added = 0
    while bound <=n :
        if i < size and nums[i] <= bound:
            bound += nums[i]
            i += 1
        else:
            added += 1
            bound <<= 1          
    return added
    
nums = [1,3]
n = 16
print minPatches(nums,n)
