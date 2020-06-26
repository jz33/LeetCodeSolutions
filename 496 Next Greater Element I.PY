'''
496. Next Greater Element I
https://leetcode.com/problems/next-greater-element-i/

You are given two arrays (without duplicates) nums1 and nums2 where nums1’s elements are subset of nums2.
Find all the next greater numbers for nums1's elements in the corresponding places of nums2.

The Next Greater Number of a number x in nums1 is the first greater number to its right in nums2.
If it does not exist, output -1 for this number.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2].
Output: [-1,3,-1]
Explanation:
    For number 4 in the first array, you cannot find the next greater number for it in the second array, so output -1.
    For number 1 in the first array, the next greater number for it in the second array is 3.
    For number 2 in the first array, there is no next greater number for it in the second array, so output -1.
    
Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4].
Output: [3,-1]
Explanation:
    For number 2 in the first array, the next greater number for it in the second array is 3.
    For number 4 in the first array, there is no next greater number for it in the second array, so output -1.
    
Note:
All elements in nums1 and nums2 are unique.
The length of both nums1 and nums2 would not exceed 1000.
'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Build a map of nums1 to update result
        valueToIndex = dict(zip(nums1, range(len(nums1))))
        res = [-1] * len(nums1)
        
        # Use stack to find all greater elements in nums2
        # Similar to 739 Daily Temperatures
        stack = [] # store values of nums2
        for val in nums2:
            while stack and val > stack[-1]:
                last = stack.pop()
                index = valueToIndex.get(last)
                if index is not None:
                    res[index] = val
            stack.append(val)

        return res
