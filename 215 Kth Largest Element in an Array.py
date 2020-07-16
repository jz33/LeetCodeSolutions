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
from random import randint

def partition(arr: List[int], left: int, right: int) -> int:
    randomIndex = randint(left, right)
    randomVal = arr[randomIndex]
    arr[right], arr[randomIndex] = arr[randomIndex], arr[right]
    pivotIndex = left
    for i in range(left, right):
        if arr[i] < randomVal:
            arr[i], arr[pivotIndex] = arr[pivotIndex], arr[i]
            pivotIndex += 1
    arr[right], arr[pivotIndex] = arr[pivotIndex], arr[right]
    return pivotIndex

def quickselect(arr: List[int], left: int, right: int, targetIndex: int) -> int:
    if left == right:
        return arr[left]
    
    pivotIndex = partition(arr, left, right)
    if pivotIndex == targetIndex:
        return arr[pivotIndex]
    elif pivotIndex < targetIndex:
        return quickselect(arr, pivotIndex + 1, right, targetIndex)
    else:
        return quickselect(arr, left, pivotIndex - 1, targetIndex)

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        Quick Select, average O(n)
        '''
        return quickselect(nums, 0, len(nums)-1, len(nums)-k)
