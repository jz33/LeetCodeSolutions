'''
Wiggle Sort
https://leetcode.com/problems/wiggle-sort/
'''
def wiggleSort(nums):
    '''
    if i is oddy, nums[i-1] <= nums[i]
    if i is even, nums[i-1] >= nums[i]
    '''
    for i in xrange(1,len(nums)):
        if ((i & 1) == 1 and nums[i-1] > nums[i]) or ((i & 1) == 0 and nums[i-1] < nums[i]):
            nums[i-1], nums[i] = nums[i], nums[i-1]

nums =  [3, 5, 2, 1, 6, 4]
wiggleSort(nums)
print nums           
