'''
493. Reverse Pairs
https://leetcode.com/problems/reverse-pairs/

Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
'''
from copy import deepcopy

def merge(arr, left, mid, right, buf):
    '''
    Regular mergo for mergesort, merge from back.
    left, mid is from left array.
    mid+1, right is from right array
    '''
    i = mid
    j = right
    k = right
    while i >= left and j > mid:
        if arr[i] <= arr[j]:
            buf[k] = arr[j]
            k -= 1
            j -= 1
        else:
            buf[k] = arr[i]
            k -= 1
            i -= 1
    
    # Put rest of right array
    while j > mid:
        buf[k] = arr[j]
        k -= 1
        j -= 1

    # Copy back
    arr[left : right+1] = buf[left : right+1]

def mergesort(arr, left, right, buf):
    if left >= right:
        return 0

    mid = left + (right - left) // 2
    count = mergesort(arr, left, mid, buf) + mergesort(arr, mid + 1, right, buf)

    # Count reversed pairs
    midBegin = mid + 1
    j = midBegin
    for i in range(left, midBegin):
        while j <= right and arr[i] > arr[j] * 2:
            j += 1
        count += j - midBegin

    merge(arr, left, mid, right, buf);
    return count

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        buf = deepcopy(nums)
        return mergesort(nums, 0, len(nums)-1, buf)
