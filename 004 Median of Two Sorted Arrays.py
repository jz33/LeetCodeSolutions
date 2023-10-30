'''
4. Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:

    nums1.length == m
    nums2.length == n
    0 <= m <= 1000
    0 <= n <= 1000
    1 <= m + n <= 2000
    -106 <= nums1[i], nums2[i] <= 106
'''
def median(arr: List[int]) -> float:
    '''
    Get median of an array
    '''
    size = len(arr)
    if size % 2 == 0:
        return (arr[size // 2 - 1] + arr[size // 2]) / 2.0
    else:
        return float(arr[size // 2 ])
        
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1:
            return median(nums2)
        if not nums2:
            return median(nums1)
        
        while not (len(nums1) < 3 or len(nums2) < 3):
            # Decide how many elements to cut.
            # Both arrays need to cut same amount of elements.
            # For array of even size, cut half size - 1; for odd size, cut half size
            cut1 = (len(nums1) - 1) // 2
            cut2 = (len(nums2) - 1) // 2
            cut = min(cut1, cut2)
            
            m1 = median(nums1)
            m2 = median(nums2)
            if m1 < m2:
                nums1 = nums1[cut:]
                nums2 = nums2[:-cut]
            else:
                nums1 = nums1[:-cut]
                nums2 = nums2[cut:]
            
        return median(sorted(nums1 + nums2))          
