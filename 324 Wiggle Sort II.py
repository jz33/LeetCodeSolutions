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
    def newIndex(self,  i):
        return (1 + (i<<1)) % (self.n | 1)
    
    def wiggleSort(self, arr: List[int]) -> None:
        '''
        https://leetcode.com/problems/wiggle-sort-ii/discuss/77682/Step-by-step-explanation-of-index-mapping-in-Java
        Use quickselect to get median, then:
        (1) elements smaller than the 'median' are put into the last even slots
        (2) elements larger than the 'median' are put into the first odd slots
        (3) the medians are put into the remaining slots.
        '''
        self.n = len(arr)
        median = quickselect(arr, (self.n >> 1))
        
        # 3-colors sort
        left = 0
        right = self.n-1
        i = 0
        while i <= right:
            ni = self.newIndex(i)
            if arr[ni] < median:
                nr = self.newIndex(right)
                arr[ni], arr[nr] = arr[nr], arr[ni]
                right -=1
            elif arr[ni] == median:
                i += 1
            else: # arr[ni] > median
                nl = self.newIndex(left)
                arr[ni], arr[nl] = arr[nl], arr[ni]
                left += 1
                i += 1
