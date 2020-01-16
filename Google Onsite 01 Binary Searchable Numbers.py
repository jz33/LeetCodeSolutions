from typing import List, Tuple
'''
https://leetcode.com/discuss/interview-question/352743/Google-or-Onsite-or-Guaranteed-Binary-Search-Numbers

Binary search is a search algorithm usually used on a sorted sequence to quickly find an element with a given value.
In this problem we will evaluate how binary search performs on data that isn't necessarily sorted.
An element is said to be binary searchable if, regardless of how the pivot is chosen the algorithm returns true. For example:

[2, 1, 3, 4, 6, 5] and target = 5, we cannot find 5. Because when the pivot is 4, we get element 6,
then right pointer will move left, so we'll lose the opportunity to find target 5.

[2, 1, 3, 4, 5, 6] and target = 5, we can find 5. Because wherever we choose the pivots, we'll find target at last.
Given an unsorted array of n distinct integers, return the number of elements that are binary searchable.

Example 1:

Input: [1, 3, 2]
Output: 1
Explanation: However we choose the pivots, we will always find the number 1 when looking for it. This does not hold for 3 and 2.
Example 2:

Input: [2, 1, 3, 5, 4, 6]
Output: 2
Explanation: 3 and 6 are the numbers guaranteed to be found.
Example 3:

Input: [1, 5, 7, 11, 12, 18]
Output: 6
Explanation: All elements in a sorted sequence are binary searchable.
Example 4:

Input: [3, 2, 1]
Output: 0
Explanation: No numbers guaranteed to be found.
Example 5:

Input: [5, 4, 6, 2, 8]
Output: 1
Explanation: Only 8 is guaranteed to be found.
Example 6:

Input: [1, 3, 2, 4, 5, 7, 6, 8]
Output: 4

'''
class Solution:
    def binarSearchableCount(self, arr: List[int]) -> int:
        '''
        If an element from unsorted array is searchable using binary search,
        it must be bigger than all its left elements, smaller than all its right elements
        '''
        #  lefts[i] is the maximum element before i (exclusive)
        lefts = [float('-inf')] + [None] * (len(arr)-1)

        #  rights[i] is the minimum element after i (exclusive)
        rights = [None] * (len(arr)-1) + [float('inf')]

        for i in range(1, len(arr)):
            lefts[i] = max(lefts[i-1], arr[i-1])

        for i in range(len(arr)-2,-1,-1):
            rights[i] = min(rights[i+1], arr[i+1])

        return sum(lefts[i] < arr[i] < rights[i] for i in range(len(arr)))


sol = Solution()
cases = [
([1, 3, 2], 1),
([2, 1, 3, 5, 4, 6], 2),
([1, 5, 7, 11, 12, 18], 6),
([3, 2, 1], 0),
([5, 4, 6, 2, 8], 1),
([1, 3, 2, 4, 5, 7, 6, 8], 4),
]
for arr, expected in cases:
    print(arr, expected, sol.binarSearchableCount(arr))
