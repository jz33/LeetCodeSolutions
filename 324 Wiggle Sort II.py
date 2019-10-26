'''
324. Wiggle Sort II

https://leetcode.com/problems/wiggle-sort-ii/
Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....
'''
import random

def partition(nums: List[int], left: int, right: int) -> int:
    '''
    @return: pivot index
    '''
    choice = random.randint(left, right)
    chosenValue = nums[choice]
    nums[right], nums[choice] = nums[choice], nums[right]

    pivot = left
    for i in range(left, right):
        if nums[i] < chosenValue:
            nums[i], nums[pivot] = nums[pivot], nums[i]
            pivot += 1

    nums[right], nums[pivot] = nums[pivot], nums[right]
    return pivot

def quickselect(nums: List[int], target: int) -> int:
    '''
    Classic quickselect
    Search @target index in @nums. @nums is modified.
    @return: the element of target index
    '''
    left = 0
    right = len(nums) - 1
    while left <= right:       
        pivot = partition(nums, left, right)
        if pivot == target:
            return nums[pivot]
        elif pivot < target:
            left = pivot + 1
        else:
            right = pivot - 1

    # target is out of range
    return None

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        quickselect(nums, (n >> 1))
        '''
        Now nums is divided by median
        Left elements are smaller, put them to even slots from end.
        This put can put medians at beginning.
        Right elements are larger, put them in odd slots from beginning.
        This put can also put medians at end.
        '''
        buf = [None] * n
        i = 0
        j = n-1 if (n & 1) == 1 else n-2
        while j >= 0:
            buf[j] = nums[i]
            i += 1
            j -= 2

        i = n-1
        j = 1
        while j < n:
            buf[j] = nums[i]
            i -= 1
            j += 2

        # Copy back
        for i in range(n):
            nums[i] = buf[i]
