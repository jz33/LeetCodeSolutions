'''
88 Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/

You are given two integer arrays nums1 and nums2,
sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function,
but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n,
where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored.
nums2 has a length of n.

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].

Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

Constraints:
    nums1.length == m + n
    nums2.length == n
    0 <= m, n <= 200
    1 <= m + n <= 200
    -109 <= nums1[i], nums2[j] <= 109

Follow up: Can you come up with an algorithm that runs in O(m + n) time?
'''
from typing import List
from heapq import heappush, heappop

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m - 1 # iterator of nums1
        j = n - 1 # iterator of nums2
        w = m + n - 1; # writer

        while i > -1 and j > -1:
            if nums1[i] < nums2[j]:
                nums1[w] = nums2[j]
                j -= 1
            else:
                nums1[w] = nums1[i];
                i -= 1
            w -= 1

        while j > -1:
            nums1[j] = nums2[j]
            j -= 1

'''
Real facebook interview question:
Merge 3 sorted arrays (having duplicates) into 1 array
https://www.1point3acres.com/bbs/thread-1040166-1-1.html
'''
def mergeArrays(arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
    result = []
    arrays = [arr1, arr2, arr3]

    heap = [] # [(value, index of the arrays, index on individual array)]
    for i, array in enumerate(arrays):
        if array:
            heappush(heap, (array[0], i, 0))

    while heap:
        value, rowIndex, colIndex = heappop(heap)
        
        if not result or value != result[-1]:
            result.append(value)

        colIndex += 1
        if colIndex < len(arrays[rowIndex]):
            heappush(heap, (arrays[rowIndex][colIndex], rowIndex, colIndex))

    return result

arr1 = [0, 1, 2]
arr2 = [0, 2, 10]
arr3 = [6, 7, 8, 8]
print(mergeArrays(arr1, arr2, arr3))

        


