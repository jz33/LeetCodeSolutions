'''
4. Median of Two Sorted Arrays
https://leetcode.com/problems/median-of-two-sorted-arrays/

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''
def median(arr: List[int]) -> float:
    '''
    @arr, size > 0
    '''
    size = len(arr)
    if (size & 1) == 0:
        return (arr[size >> 1] + arr[(size >> 1) - 1]) / 2.0
    else:
        return float(arr[size >> 1])
        
class Solution:
    def baseCase(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        Either len(nums1) < 3 or len(nums2) < 3
        A lasy way. Can use binary search.
        '''
        return median(sorted(nums1 + nums2))
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1:
            return median(nums2)
        if not nums2:
            return median(nums1)
        
        while not (len(nums1) < 3 or len(nums2) < 3):
            s1 = len(nums1)
            cut1 = (s1 >> 1) if (s1 & 1) else (s1 >> 1) - 1
            s2 = len(nums2)
            cut2 = (s2 >> 1) if (s2 & 1) else (s2 >> 1) - 1
            cut = min(cut1, cut2) # how many elements need to abandon, same for both array
            
            m1 = median(nums1)
            m2 = median(nums2)
            if m1 < m2:
                nums1 = nums1[cut:]
                nums2 = nums2[:-cut]
            else:
                nums1 = nums1[:-cut]
                nums2 = nums2[cut:]
                
        return self.baseCase(nums1, nums2)       
