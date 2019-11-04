'''
327. Count of Range Sum
https://leetcode.com/problems/count-of-range-sum/

Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive.
Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Example:

Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3 
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2
'''
def mergesort(arr, lower, upper, left, right):
    if left >= right:
        return 0

    mid = left + (right - left) // 2
    count = mergesort(arr, lower, upper, left, mid) + mergesort(arr, lower, upper, mid + 1, right)

    # Count of range sum
    midBegin = mid + 1
    lo, hi = midBegin, midBegin
    for e in arr[left : midBegin]:
        # This is to count how many sum ranges smaller than lower
        while lo <= right and arr[lo] - e < lower:
            lo += 1

        # This is to count how many sum ranges smaller or equal to upper
        while hi <= right and arr[hi] - e <= upper:
            hi += 1

        count += hi - lo

    # Use a lasy simple sort to merge
    arr[left : right+1] = sorted(arr[left : right+1])
    return count

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # Build accumulation array
        arr = [0] * (len(nums)+1)
        for i in range(len(nums)):
            arr[i+1] = arr[i] + nums[i]

        return mergesort(arr, lower, upper, 0, len(arr)-1)
