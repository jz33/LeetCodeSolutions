'''
768. Max Chunks To Make Sorted II
https://leetcode.com/problems/max-chunks-to-make-sorted-ii/

This question is the same as "Max Chunks to Make Sorted" except the integers of the given array are
not necessarily distinct, the input array could be up to length 2000, and the elements could be up to 10**8.

Given an array arr of integers (not necessarily distinct), we split the array into some number of "chunks" (partitions),
and individually sort each chunk.  After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

Example 1:

Input: arr = [5,4,3,2,1]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.

Example 2:

Input: arr = [2,1,3,4,4]
Output: 4
Explanation:
We can split into two chunks, such as [2, 1], [3, 4, 4].
However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.
Note:

arr will have length in range [1, 2000].
arr[i] will be an integer in range [0, 10**8].
'''
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        '''
        Each time there is a cut that cuts the array to left branch and
        right branch, and all left elements are smaller than right,
        then there can be a new chunk
        '''
        #  lefts[i] is the maximum element before i (inclusive)
        lefts = [arr[0]] + [None] * (len(arr)-1)

        #  rights[i] is the minimum element after i (inclusive)
        rights = [None] * (len(arr)-1) + [arr[-1]]

        for i in range(1, len(arr)):
            lefts[i] = max(lefts[i-1], arr[i])

        for i in range(len(arr)-2,-1,-1):
            rights[i] = min(rights[i+1], arr[i])

        return sum(lefts[i] <= rights[i+1] for i in range(len(arr)-1)) + 1
