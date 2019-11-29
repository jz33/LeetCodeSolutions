'''
215. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array/

Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order,
not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''
import random

def partition(arr, left, right) -> int:
    rd = random.randint(left, right)
    rv = arr[rd]
    pivot = left
    arr[rd], arr[right] = arr[right], arr[rd]
    for i in range(left, right):
        if arr[i] < rv:
            arr[pivot], arr[i] = arr[i], arr[pivot]
            pivot += 1
    arr[pivot], arr[right] = arr[right], arr[pivot]
    return pivot

def quickselect(arr, left, right, targetIndex) -> int:
    if left >= right:
        return arr[left]
    pivot = partition(arr, left, right)
    if pivot == targetIndex:
        return arr[pivot]
    elif pivot < targetIndex:
        return quickselect(arr, pivot + 1, right, targetIndex)
    else:
        return quickselect(arr, left, pivot - 1, targetIndex)
    
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return quickselect(nums, 0, len(nums)-1, len(nums) - k)
